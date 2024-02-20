import numpy as np
import cv2 as cv
path = 'static/img'

def features(image, filename):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    gray = np.float32(gray)
    dst = cv.cornerHarris(gray, 2, 3, 0.04)

    # Result is dilated for marking the corners, not important
    dst = cv.dilate(dst, None)

    # Threshold for an optimal value, it may vary depending on the image.
    image[dst > 0.01 * dst.max()] = [0, 0, 255]
    name = path + "/" + filename + ".jpg"
    cv.imwrite(name, image)
    return name