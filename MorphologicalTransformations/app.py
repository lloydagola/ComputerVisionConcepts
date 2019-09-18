import cv2
import numpy
from matplotlib import pyplot

original_image = cv2.cv2.imread("colored_balls.jpg", cv2.cv2.IMREAD_GRAYSCALE)
_, mask = cv2.cv2.threshold(original_image, 220, 255, cv2.cv2.THRESH_BINARY_INV)

titles = ['image', 'mask']
images = [original_image, mask]

for i in range(2):
    pyplot.subplot(1, 2, i+1), pyplot.imshow(images[i], 'gray')
    pyplot.title(titles[i])
    pyplot.xticks([]), pyplot.yticks([])

pyplot.show()