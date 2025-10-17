import cv2

def capture_image():
    # Open the webcam (0 = default camera)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam")
        exit()

    # Read a single frame
    ret, frame = cap.read()

    if ret:
        # Display the captured frame
        cv2.imshow("Captured Image", frame)

        # Save the image to your computer
        cv2.imwrite("captured_image.jpg", frame)
        print("Image saved as 'captured_image.jpg'")

        # Wait until a key is pressed, then close window
        cv2.waitKey(0)
    else:
        print("Error: Could not capture image")

    # Release the webcam and close windows
    cap.release()
    cv2.destroyAllWindows()
