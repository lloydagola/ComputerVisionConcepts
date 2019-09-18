import cv2
import numpy
from matplotlib import pyplot

original_image = cv2.cv2.imread("colored_balls.jpg", cv2.cv2.IMREAD_GRAYSCALE)
_, mask = cv2.cv2.threshold(original_image, 220, 255, cv2.cv2.THRESH_BINARY_INV)

kernal = numpy.ones((2,2), numpy.uint8)
dilation = cv2.cv2.dilate(mask, kernal)

titles = ['image', 'mask', 'dilation']
images = [original_image, mask, dilation]

for i in range(3):
    pyplot.subplot(1, 3, i+1), pyplot.imshow(images[i], 'gray')
    pyplot.title(titles[i])
    pyplot.xticks([]), pyplot.yticks([])

pyplot.show()