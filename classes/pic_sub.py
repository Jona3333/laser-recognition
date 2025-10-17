import cv2
import numpy as np
import os

class LaserDotDetector:
    def __init__(self, min_area=5, max_area=200, threshold=10):
        self.min_area = min_area
        self.max_area = max_area
        self.threshold = threshold

    def find_laser_dot(self, diff_img, show=False):
        if len(diff_img.shape) == 3:
            gray = cv2.cvtColor(diff_img, cv2.COLOR_BGR2GRAY)
        else:
            gray = diff_img.copy()
        _, thresh = cv2.threshold(gray, self.threshold, 255, cv2.THRESH_BINARY)
        kernel = np.ones((3, 3), np.uint8)
        clean = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
        contours, _ = cv2.findContours(clean, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        laser_dots = []
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if self.min_area < area < self.max_area:
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


    def diff_images(self, image_path1, image_path2, show=False, save=False):
        img1 = cv2.imread(image_path1)
        img2 = cv2.imread(image_path2)
        if img1 is None or img2 is None:
            raise ValueError("One or both image paths are invalid or images could not be loaded.")
        if img1.shape != img2.shape:
            raise ValueError("Images must be the same size and shape.")
        diff = cv2.absdiff(img1, img2)
        if save:
            images_dir = os.path.dirname(image_path1)
            file1_name = os.path.basename(image_path1).split('.')[0]
            file2_name = os.path.basename(image_path2).split('.')[0]
            output_path = os.path.join(images_dir, f"diff_{file1_name}_{file2_name}.jpg")
            cv2.imwrite(output_path, diff)
            print(f"Difference image saved to: {output_path}")
        if show:
            cv2.imshow("Difference", diff)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        return diff

    def find_laser_dot_old(self, diff_img, show=False):
        if len(diff_img.shape) == 3:
            gray = cv2.cvtColor(diff_img, cv2.COLOR_BGR2GRAY)
        else:
            gray = diff_img.copy()
        _, thresh = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)
        kernel = np.ones((3, 3), np.uint8)
        clean = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
        contours, _ = cv2.findContours(clean, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        laser_dots = []
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if self.min_area < area < self.max_area:
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

    def save_laser_dot_image(self, diff_img, laser_dots, output_path):
        if len(diff_img.shape) == 2:
            out_img = cv2.cvtColor(diff_img, cv2.COLOR_GRAY2BGR)
        else:
            out_img = diff_img.copy()
        for (cx, cy) in laser_dots:
            cv2.circle(out_img, (cx, cy), 8, (0, 255, 0), 2)
        cv2.imwrite(output_path, out_img)
        print(f"Laser dot image saved to: {output_path}")

# Example usage:
# detector = LaserDotDetector(min_area=1, max_area=500)
# diff = detector.diff_images('images/3.jpg', 'images/4.jpg', show=True, save=True)
# laser_points = detector.find_laser_dot(diff, show=True)
# detector.save_laser_dot_image(diff, laser_points, os.path.join('images', 'laser_dots_circled.jpg'))
