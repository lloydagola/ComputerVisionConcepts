import cv2
import numpy as numpy

image = cv2.cv2.imread("gradient.png", 0)
_, thresholdResult = cv2.cv2.threshold(image, 127, 255, cv2.cv2.THRESH_BINARY) 

cv2.cv2.imshow("Original", image)
cv2.cv2.imshow("ThreSH_BINARY", thresholdResult)

cv2.cv2.waitKey(0)
cv2.cv2.destroyAllWindows()

