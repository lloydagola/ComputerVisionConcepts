import numpy as np
import cv2

def do_stuff(x):
    print(x)

# Create a black window_name, a window
cv2.cv2.namedWindow('window_name')

cv2.cv2.createTrackbar('trackbar_name', 'window_name', 10, 400, do_stuff)
cv2.cv2.createTrackbar('toggle_grayscale', 'window_name', 0, 1, do_stuff)
cv2.cv2.createTrackbar("BlueTrackbar", "window_name", 0, 255, do_stuff)
cv2.cv2.createTrackbar("GreenTrackbar", "window_name", 0, 255, do_stuff)
cv2.cv2.createTrackbar("RedTrackbar", "window_name", 0, 255, do_stuff)

while(1):
    img = cv2.cv2.imread('pexels.jpeg')

    some_value = cv2.cv2.getTrackbarPos('trackbar_name', 'window_name')
    toggle_grayscale = cv2.cv2.getTrackbarPos('toggle_grayscale', 'window_name')

    blueValue = cv2.cv2.getTrackbarPos("BlueTrackbar", "window_name")
    greenValue = cv2.cv2.getTrackbarPos("GreenTrackbar", "window_name")
    redValue = cv2.cv2.getTrackbarPos("RedTrackbar", "window_name")
    
    cv2.cv2.putText(img, str(some_value), (50, 150), cv2.cv2.FONT_HERSHEY_SIMPLEX, 6, (0, 0, 255), 10)

    if cv2.cv2.waitKey(1) & 0xFF == 27:
        break

    if toggle_grayscale == 0:
        img[:] = [blueValue, greenValue, redValue]
    else:
       img = cv2.cv2.cvtColor(img, cv2.cv2.COLOR_BGR2GRAY)

    img = cv2.cv2.imshow('window_name',img)

cv2.cv2.destroyAllWindows()