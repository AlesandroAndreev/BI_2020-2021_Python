import numpy as np
import cv2 as cv

image = cv.imread(input("Write way to image: "))

def circle_detect(img):

    output = img.copy()

    bgr_to_gray = cv.medianBlur(cv.cvtColor(img, cv.COLOR_BGR2GRAY), 5)

    circles = cv.HoughCircles(bgr_to_gray, cv.HOUGH_GRADIENT, 1, 20,
                              param1=40, param2=46, minRadius=0, maxRadius=0)

    detected_circles = np.uint16(np.around(circles))

    for (x, y ,r) in detected_circles[0, :]:
        cv.circle(output, (x, y), r, (0, 0, 0), 3)
        cv.circle(output, (x, y), 2, (0, 255, 255), 3)
    return output


detect = circle_detect(image)

cv.imshow('Detecting circles',detect)
cv.waitKey(0)
cv.destroyAllWindows()
