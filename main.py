import math
import os
import time
import cv2

import classes.Params as par
from classes.color_rec import RedDetector
from classes.pic_sub import LaserDotDetector

#functions:
def capture_image(name):
    # Open the webcam (0 = default camera)
    cap = cv2.VideoCapture(1)

    if not cap.isOpened():
        print("Error: Could not open webcam")
        exit()

    # Read a single frame
    ret, frame = cap.read()

    if ret:
        # Save the image to your computer
        cv2.imwrite("images/" + name + ".jpg", frame)
        print("Image saved as", name)

        # Wait until a key is pressed, then close window
        cv2.waitKey(0)
    else:
        print("Error: Could not capture image")

    # Release the webcam and close windows
    cap.release()
    cv2.destroyAllWindows()

    return frame



# capture first image
img1 = capture_image("1")
time.sleep(0.5)
img2 = capture_image("2")

# turn off laser


# capture second image


# find 4 dots from 2 pictures
detector = LaserDotDetector(min_area=1, max_area=500, threshold=90)
diff = detector.diff_images('images/1.jpg', 'images/2.jpg', save=True)
laser_points = detector.find_laser_dot(diff)
detector.save_laser_dot_image(diff, laser_points, os.path.join('images', 'laser_dots_circled.jpg'))

# detector2 = RedDetector()
# centers2 = detector.find_red_dots('images/1.jpg', show=True, save_path='images/red_dots_found.jpg')
# print("Dot centers:", centers2)
# mask = detector.find_red_areas("images/1.jpg", show=True, save_path="red_mask.jpg")



# find dist between those 2

# def pixels_dist(x1,y1,x2,y2):
#     square = (x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)
#     return math.sqrt(square)


def pixels_dist(x1, y1, x2, y2):
    return abs(x1-x2)



# find length to wall
def dist(pixels):
    return par.Params.A * 1/pixels

# Example usage with the first two detected laser points
if len(laser_points) >= 2:
    x1, y1 = laser_points[0]
    x2, y2 = laser_points[1]
    pixel_dist = pixels_dist(x1, y1, x2, y2)
    print("Pixel distance between first two dots:", pixel_dist)
    length = dist(pixel_dist)
    print(length)
