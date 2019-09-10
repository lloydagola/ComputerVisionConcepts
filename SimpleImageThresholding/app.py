import cv2
import numpy as numpy

image = cv2.cv2.imread("gradient.png", 0)
_, thresholdResult = cv2.cv2.threshold(image, 50, 255, cv2.cv2.THRESH_BINARY) 
_, thresholdResult2 = cv2.cv2.threshold(image, 200, 255, cv2.cv2.THRESH_BINARY_INV) 
_, thresholdResult3 = cv2.cv2.threshold(image, 50, 255, cv2.cv2.THRESH_TRUNC) 
_, thresholdResult4 = cv2.cv2.threshold(image, 50, 255, cv2.cv2.THRESH_TOZERO) 
_, thresholdResult5 = cv2.cv2.threshold(image, 50, 255, cv2.cv2.THRESH_TOZERO_INV) 


cv2.cv2.imshow("Original", image)
cv2.cv2.imshow("THRESH_BINARY", thresholdResult)
cv2.cv2.imshow("THRESH_BINARY_INV", thresholdResult2)
cv2.cv2.imshow("THRESH_TRUNC", thresholdResult3)
cv2.cv2.imshow("THRESH_TOZERO", thresholdResult4)
cv2.cv2.imshow("THRESH_TOZERO_INV", thresholdResult5)

cv2.cv2.waitKey(0)
cv2.cv2.destroyAllWindows()

