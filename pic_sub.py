import cv2
import numpy as np
import Params
def diff_images(image_path1, image_path2, show=False):
    # Load the images
    img1 = cv2.imread(image_path1)
    img2 = cv2.imread(image_path2)

    # Check if images loaded properly
    if img1 is None or img2 is None:
        raise ValueError("One or both image paths are invalid or images could not be loaded.")

    # Resize to the same shape if needed (optional, but practical)
    if img1.shape != img2.shape:
        raise ValueError("Images must be the same size and shape.")

    # Compute the absolute difference
    diff = cv2.absdiff(img1, img2)

    # Optionally show the result
    if show:
        cv2.imshow("Difference", diff)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return diff


import cv2
import numpy as np

def find_laser_dot(diff_img, show=False, min_area=5, max_area=200):
    """
    Finds a small dot (e.g., laser) in a difference image.
    :param diff_img: Image from cv2.absdiff(img1, img2), either grayscale or color.
    :param show: Whether to display the image with detection drawn.
    :param min_area: Minimum area of detected dot.
    :param max_area: Maximum area of detected dot.
    :return: List of (x, y) coordinates of detected dots.
    """
    # If it's a color image, convert to grayscale
    if len(diff_img.shape) == 3:
        gray = cv2.cvtColor(diff_img, cv2.COLOR_BGR2GRAY)
    else:
        gray = diff_img.copy()

    # Threshold the difference to get binary mask of changes
    _, thresh = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)

    # Clean small noise
    kernel = np.ones((3, 3), np.uint8)
    clean = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

    # Find contours (each contour is a change area)
    contours, _ = cv2.findContours(clean, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    laser_dots = []

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if min_area < area < max_area:
            # Get center of the contour
            M = cv2.moments(cnt)
            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                laser_dots.append((cx, cy))
                if show:
                    cv2.circle(diff_img, (cx, cy), 5, (0, 255, 0), 2)

    if show:
        cv2.imshow("Laser Dot Detection", diff_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return laser_dots


diff = diff_images("images/5.jpg", "images/6.jpg", show=True)
laser_points = find_laser_dot(diff, show=True)
print("Laser detected at:", laser_points)
