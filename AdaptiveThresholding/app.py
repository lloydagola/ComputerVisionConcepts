import cv2
import numpy as np

original_image = cv2.cv2.imread("sudoku.jpg", 0)
_, threshold_result = cv2.cv2.threshold(original_image, 127, 255, cv2.cv2.THRESH_BINARY)

cv2.cv2.imshow("original", original_image)
cv2.cv2.imshow("threshold", threshold_result)

cv2.cv2.waitKey(0)
cv2.cv2.destroyAllWindows()
