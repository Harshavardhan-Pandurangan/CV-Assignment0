# code to capture images from the camera and save them locally

import cv2
import os

# Create a directory to save the captured images
output_folder = 'cam_captures'
os.makedirs(output_folder, exist_ok=True)

# Open webcam (0 for built-in webcam, 1 for external webcam)
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

try:
    # Loop to capture and save images until interrupted
    while True:
        ret, frame = cap.read()

        if ret:
            cv2.imshow('Camera Feed', frame)
            cv2.waitKey(1)
            image_filename = f"{output_folder}/{len(os.listdir(output_folder)) + 1}.png"
            cv2.imwrite(image_filename, frame)

# Break the loop when interrupted
except KeyboardInterrupt:
    print("Capture interrupted by user.")

cap.release()
