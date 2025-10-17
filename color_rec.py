import cv2
import numpy as np

def find_red_areas(image_path, show=False):
    # Load the image
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError("Image could not be loaded.")

    # Convert BGR to HSV color space
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Define red color ranges in HSV
    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])

    lower_red2 = np.array([160, 100, 100])
    upper_red2 = np.array([179, 255, 255])

    # Create masks for red
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

    # Combine masks
    red_mask = cv2.bitwise_or(mask1, mask2)

    # Optional: clean up noise
    kernel = np.ones((3, 3), np.uint8)
    red_mask = cv2.morphologyEx(red_mask, cv2.MORPH_OPEN, kernel)
    red_mask = cv2.morphologyEx(red_mask, cv2.MORPH_DILATE, kernel)

    if show:
        cv2.imshow("Red Areas", red_mask)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return red_mask

mask = find_red_areas("images/7.jpg", show=True)
cv2.imwrite("red_mask.jpg", mask)
