# Hand Gesture-Based Brightness Control

This Python project uses computer vision techniques to control screen brightness dynamically through hand gestures. The system leverages OpenCV for video capture and hand tracking, 
while `screen_brightness_control` is used to modify the brightness settings.

---

## Setup Instructions

1. **Install Dependencies**:
   ```bash
   pip install opencv-python numpy screen-brightness-control
   ```

2. **Verify the Custom Module**:
   - Place `handlTrackingModule.py` in the same directory as the script.
   - Ensure it provides the `handDetector` class with the following methods:
     - `findHands(img)`
     - `findPosition(img, draw)`

3. **Run the Script**:
   ```bash
   python script_name.py
   ```


## Usage

1. Start the script and position your hand in front of the camera.
2. Adjust the distance between your thumb and index finger to control brightness:
   - Closer fingers = Lower brightness
   - Further apart = Higher brightness
3. Press `q` to quit the application.

---

## Troubleshooting

1. **Camera Not Detected**:
   - Ensure your webcam is functional and accessible.
   - Check camera permissions on your system.

2. **Hand Not Detected**:
   - Ensure adequate lighting.
   - Position your hand within the camera's frame.

3. **Brightness Not Changing**:
   - Verify `screen_brightness_control` is installed and supports your system.
   - Check for any errors in the `handlTrackingModule` implementation.

Happy Coding! 🎉
