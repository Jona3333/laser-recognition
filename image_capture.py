import time
import cv2
import os

def capture_image(name):
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    images_dir = os.path.join(script_dir, "images")
    os.makedirs(images_dir, exist_ok=True)
    save_path = os.path.join(images_dir, f"{name}.jpg")

    # Open the webcam (1 = default camera)
    cap = cv2.VideoCapture(1)

    if not cap.isOpened():
        print("Error: Could not open webcam")
        exit()

    # Read a single frame
    ret, frame = cap.read()

    if ret:
        print(save_path)
        # Display the captured frame
        cv2.imshow("Captured Image", frame)

        # Save the image to /images/name.jpg
        cv2.imwrite(save_path, frame)
        print(f"Image saved as '{save_path}'")

        # Wait until a key is pressed, then close window
        cv2.waitKey(0)
    else:
        print("Error: Could not capture image")

    # Release the webcam and close windows
    cap.release()
    cv2.destroyAllWindows()

    return frame

def images():
    capture_image("1")
    time.sleep(0.5)
    capture_image("2")