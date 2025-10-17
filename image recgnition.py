import cv2
import numpy as np
from matplotlib import pyplot as plt


def compare_pixels(pixel1, pixel2):
    return abs(pixel1[0] - pixel2[0]) + abs(pixel1[1] - pixel2[1]) + abs(pixel1[2] - pixel2[2])

def take_picture():
    # Initialize webcam (0 = default camera)
    cam = cv2.VideoCapture(0)

    # Capture one frame
    ret, frame = cam.read()

    if ret:
        cv2.imshow("Captured", frame)
        cv2.imwrite("captured_image.png", frame)
        cv2.waitKey(0)
        cv2.destroyWindow("Captured")
    else:
        print("Failed to capture image.")

    cam.release()

def my_detection(img):
    # print(img[975][795])
    found = False
    radius = 0
    while not found:
        radius += 1
        for i in range(100):
            if found: break
            for j in range(150):
                if found: break
                y_pixel, x_pixel = i + 930, j + 720
                if compare_pixels(img[y_pixel][x_pixel], img[y_pixel - radius][x_pixel - radius]) > 30 and\
                    compare_pixels(img[y_pixel][x_pixel], img[y_pixel + radius][x_pixel - radius]) > 30 and\
                    compare_pixels(img[y_pixel][x_pixel], img[y_pixel - radius][x_pixel + radius]) > 30 and\
                    compare_pixels(img[y_pixel][x_pixel], img[y_pixel + radius][x_pixel + radius]) > 30:
                    found = True
                    print(" width:", y_pixel, "height:", x_pixel, " radius:", radius)
                    break
                # print(img[i][j], end=" ")
            # print()

def main():
    my_detection(cv2.imread("captured_image.png"))


if __name__ == '__main__':
    main()