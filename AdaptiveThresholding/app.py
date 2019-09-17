import cv2
import numpy as np

original_image = cv2.cv2.imread("sudoku.jpg", 0)
_, regular_threshold_result = cv2.cv2.threshold(original_image, 127, 255, cv2.cv2.THRESH_BINARY)
adaptive_threshold_result = cv2.cv2.adaptiveThreshold(original_image, 255, cv2.cv2.ADAPTIVE_THRESH_MEAN_C, cv2.cv2.THRESH_BINARY, 11, 2)
adaptive_threshold_gaussian_result = cv2.cv2.adaptiveThreshold(original_image, 255, cv2.cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.cv2.THRESH_BINARY, 11, 2)

cv2.cv2.imshow("original", original_image)
cv2.cv2.imshow("regular_threshold", regular_threshold_result)
cv2.cv2.imshow("adaptive_threshold", adaptive_threshold_result)
cv2.cv2.imshow("adaptive_threshold_gausian", adaptive_threshold_gaussian_result)

cv2.cv2.waitKey(0)
cv2.cv2.destroyAllWindows()
