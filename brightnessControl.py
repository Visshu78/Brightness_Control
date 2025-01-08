import cv2
import time
import numpy as np
import handlTrackingModule as htm  # Ensure this module is available
import math
import screen_brightness_control as sbc

# camera initailization
wCam, hCam = 640, 488
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0
detector = htm.handDetector(detectionCon=0.8)

brightness = sbc.get_brightness()
minBrightness = 0
maxBrightness = 100
bright = 0
brightBar = 400
brightPer = 0

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmlist = detector.findPosition(img, draw=False)

    if len(lmlist) != 0:
        # Extracting thumb and index finger positions
        x1, y1 = lmlist[4][1], lmlist[4][2]     #thumb
        x2, y2 = lmlist[8][1], lmlist[8][2]     #index finger
        x3, y3 = lmlist[12][1],lmlist[12][2]        #Middle finger
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        # Drawing shapes
        cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x3, y3), 15, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
        cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

        # Calculating length between two fingers
        length = math.hypot(x2 - x1, y2 - y1)

        # Convert length to brightness range
        bright = np.interp(length, [50, 300], [minBrightness, maxBrightness])
        brightBar = np.interp(length, [50, 300], [400, 125])
        brightPer = np.interp(length, [50, 300], [0, 100])
        print(int(length), bright)

        # Set volume level
        sbc.set_brightness(int (bright))

        # Visual feedback when fingers are close
        if length < 50:
            cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)

    # Volume bar and percentage display (nothing to change here)
    cv2.rectangle(img, (50, 150), (85, 400), (0, 255, 0), 3)
    cv2.rectangle(img, (50, int(brightBar)), (85, 400), (0, 255, 0), cv2.FILLED)

    cv2.putText(img, 'Brightness: {}%'.format(int(brightPer)), (40, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 3)

    # FPS Calculation
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, 'FPS: {}'.format(int(fps)), (40, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 3)

    # Display Image
    cv2.imshow("Img", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break