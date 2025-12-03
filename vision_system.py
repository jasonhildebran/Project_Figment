import time
import cv2
import numpy as np
from picamzero import Camera # Using the simpler wrapper if available, or raw Picamera2

# Try importing the official library
try:
    from picamera2 import Picamera2
except ImportError:
    print("CRITICAL ERROR: Picamera2 not found!")
    print("Did you recreate the venv with '--system-site-packages'?")
    exit()

class Eye:
    def __init__(self):
        print("[VISION] Initializing Picamera2...")
        
        # Configure the Camera
        self.picam2 = Picamera2()
        
        # Configure for 640x480 (Fast processing)
        config = self.picam2.create_preview_configuration(main={"size": (640, 480), "format": "BGR888"})
        self.picam2.configure(config)
        self.picam2.start()

        # Load Face Detection (Standard OpenCV)
        cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        self.face_cascade = cv2.CascadeClassifier(cascade_path)
        
        print("[VISION] Camera Online.")

    def look(self):
        # 1. Grab the frame directly into an OpenCV-compatible array
        # This is INSTANT because it uses the hardware memory buffer
        try:
            frame = self.picam2.capture_array()
        except Exception as e:
            print(f"[ERROR] Capture failed: {e}")
            return None

        # 2. FLIP (Fixing upside down) - REMOVED as per user request
        # frame = cv2.flip(frame, -1)

        # 3. DEBUG: Save image
        # Save every 20th frame to check feed
        if int(time.time() * 10) % 20 == 0:
            cv2.imwrite("robot_view.jpg", frame)

        # 4. Detect Faces
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.1, 3)
        
        if len(faces) > 0:
            largest = max(faces, key=lambda r: r[2] * r[3])
            x, y, w, h = largest
            return (x + w//2, y + h//2)
        
        return None

    def close(self):
        self.picam2.stop()
        self.picam2.close()

def map_range(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

if __name__ == "__main__":
    eye = Eye()
    print("System Online. Dots = Running.")
    try:
        while True:
            res = eye.look()
            if res:
                x_pixel = res[0]
                neck_angle = map_range(x_pixel, 0, 640, 135, 45)
                print(f" -> I SEE YOU! [X: {x_pixel}, Y: {res[1]}] Neck Command: {neck_angle}")
            else:
                print(".", end="", flush=True)
            time.sleep(0.05)
    except KeyboardInterrupt:
        print("\nStopping")
        eye.close()