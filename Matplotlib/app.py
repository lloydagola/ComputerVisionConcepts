import cv2
from matplotlib import pyplot


original_image = cv2.cv2.imread("pexels.jpeg")
cv2.cv2.imshow("original image", original_image)

pyplot.imshow(original_image)
pyplot.show()

cv2.cv2.waitKey(0)
cv2.cv2.destroyAllWindows()