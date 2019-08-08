import cv2
import numpy as np

picture = cv2.cv2.imread("picture.png")
black_image = np.zeros((250, 500, 3), np.uint8)
white_rectangle = cv2.cv2.rectangle(black_image, (200, 0), (300, 100), (255,255,255), -1)

cv2.cv2.imshow("Black", black_image)
cv2.cv2.imshow("Picture", picture)

cv2.cv2.waitKey(0)
cv2.cv2.destroyAllWindows()