import cv2
import numpy as np

class RedDetector:
    def __init__(self):
        # HSV ranges for red detection
        self.lower_red1 = np.array([0, 70, 70])
        self.upper_red1 = np.array([20, 255, 255])
        self.lower_red2 = np.array([160, 70, 70])
        self.upper_red2 = np.array([179, 255, 255])
        self.kernel = np.ones((3, 3), np.uint8)

    def find_red_areas(self, image_path, show=False, save_path=None):
        img = cv2.imread(image_path)
        if img is None:
            raise ValueError("Image could not be loaded.")
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        mask1 = cv2.inRange(hsv, self.lower_red1, self.upper_red1)
        mask2 = cv2.inRange(hsv, self.lower_red2, self.upper_red2)
        red_mask = cv2.bitwise_or(mask1, mask2)
        red_mask = cv2.morphologyEx(red_mask, cv2.MORPH_OPEN, self.kernel)
        red_mask = cv2.morphologyEx(red_mask, cv2.MORPH_DILATE, self.kernel)
        if show:
            cv2.imshow("Red Areas", red_mask)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        if save_path:
            cv2.imwrite(save_path, red_mask)
        return red_mask

    def find_red_dots(self, image_path, show=False, save_path=None, max_dots=2):
        img = cv2.imread(image_path)
        if img is None:
            raise ValueError("Image could not be loaded.")
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        mask1 = cv2.inRange(hsv, self.lower_red1, self.upper_red1)
        mask2 = cv2.inRange(hsv, self.lower_red2, self.upper_red2)
        red_mask = cv2.bitwise_or(mask1, mask2)
        red_mask = cv2.morphologyEx(red_mask, cv2.MORPH_OPEN, self.kernel)
        red_mask = cv2.morphologyEx(red_mask, cv2.MORPH_DILATE, self.kernel)
        contours, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=cv2.contourArea, reverse=True)[:max_dots]
        centers = []
        for cnt in contours:
            M = cv2.moments(cnt)
            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                centers.append((cx, cy))
                cv2.circle(img, (cx, cy), 10, (0, 255, 0), 2)
        if show:
            cv2.imshow("Red Dots", img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        if save_path:
            cv2.imwrite(save_path, img)
        return centers

# Example usage:
# detector = RedDetector()
# centers = detector.find_red_dots('images/1.jpg', show=True, save_path='images/red_dots_found.jpg')
# print("Dot centers:", centers)
# mask = detector.find_red_areas("images/1.jpg", show=True, save_path="red_mask.jpg")
