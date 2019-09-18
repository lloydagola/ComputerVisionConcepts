import cv2
import numpy
from matplotlib import pyplot


def display_colored_balls():
    original_image = cv2.cv2.imread("colored_balls.jpg", cv2.cv2.IMREAD_GRAYSCALE)
    _, mask = cv2.cv2.threshold(original_image, 220, 255, cv2.cv2.THRESH_BINARY_INV)

    kernal = numpy.ones((2,2), numpy.uint8)
    dilation = cv2.cv2.dilate(mask, kernal, iterations=2)
    erosion = cv2.cv2.erode(mask, kernal, iterations=1)
    opening = cv2.cv2.morphologyEx(mask, cv2.cv2.MORPH_OPEN, kernal)
    closing = cv2.cv2.morphologyEx(mask, cv2.cv2.MORPH_CLOSE, kernal)
    morphologicalGradient = cv2.cv2.morphologyEx(mask, cv2.cv2.MORPH_GRADIENT, kernal)
    tophat = cv2.cv2.morphologyEx(mask, cv2.cv2.MORPH_TOPHAT, kernal)

    titles = ['image', 'mask', 'dilation', 'erosion', 'opening','closing','morphologicalGradient', 'tophat']
    images = [original_image, mask, dilation, erosion, opening, closing,morphologicalGradient, tophat]

    for i in range(8):
        pyplot.subplot(3, 3, i+1), pyplot.imshow(images[i], 'gray')
        pyplot.title(titles[i])
        pyplot.xticks([]), pyplot.yticks([])

    pyplot.show()

def display_writing():
    original_image = cv2.cv2.imread("text.png", cv2.cv2.IMREAD_GRAYSCALE)

    kernal = numpy.ones((2,2), numpy.uint8)
    dilation = cv2.cv2.dilate(original_image, kernal, iterations=2)
    erosion = cv2.cv2.erode(original_image, kernal, iterations=1)
    opening = cv2.cv2.morphologyEx(original_image, cv2.cv2.MORPH_OPEN, kernal)
    closing = cv2.cv2.morphologyEx(original_image, cv2.cv2.MORPH_CLOSE, kernal)
    morphologicalGradient = cv2.cv2.morphologyEx(original_image, cv2.cv2.MORPH_GRADIENT, kernal)
    tophat = cv2.cv2.morphologyEx(original_image, cv2.cv2.MORPH_TOPHAT, kernal)

    titles = ['image', 'dilation', 'erosion', 'opening','closing','morphologicalGradient', 'tophat']
    images = [original_image, dilation, erosion, opening, closing,morphologicalGradient, tophat]

    for i in range(7):
        pyplot.subplot(3, 3, i+1), pyplot.imshow(images[i], 'gray')
        pyplot.title(titles[i])
        pyplot.xticks([]), pyplot.yticks([])

    pyplot.show()

display_colored_balls()
display_writing()