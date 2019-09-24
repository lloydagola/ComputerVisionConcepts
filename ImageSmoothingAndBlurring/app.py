import cv2
import numpy
from matplotlib import pyplot

img = cv2.cv2.imread("lena.png")
img = cv2.cv2.cvtColor(img, cv2.cv2.COLOR_BGR2RGB)

kernel = numpy.ones((5,5),  numpy.float32)/25
filter2D = cv2.cv2.filter2D(img, -1, kernel)
blur = cv2.cv2.blur(img, (5, 5))
gaussian_blur = cv2.cv2.GaussianBlur(img, (5,5), 0)
median_blur = cv2.cv2.medianBlur(img, 5)
bilateral_filter = cv2.cv2.bilateralFilter(median_blur, 9, 75, 75)

titles = ['image', 'filter2D', 'blur', 'Gaussian blur', 'Median blur', 'Bilateral filter']
images = [img, filter2D, blur, gaussian_blur, median_blur, bilateral_filter]

for i in range(6):
    pyplot.subplot(2, 3, i + 1), pyplot.imshow(images[i], 'gray')
    pyplot.title(titles[i])
    pyplot.xticks([]), pyplot.yticks([])

pyplot.show()

 