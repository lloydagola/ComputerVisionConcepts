import cv2
import numpy
from matplotlib import pyplot

original_image = cv2.cv2.imread("colored_balls.jpg", cv2.cv2.IMREAD_GRAYSCALE)

titles = ['image']
images = [original_image]

for i in range(1):
    pyplot.subplot(1, 1, i+1), pyplot.imshow(images[i], 'gray')
    pyplot.title(titles[i])
    pyplot.xticks([]), pyplot.yticks([])

pyplot.show()