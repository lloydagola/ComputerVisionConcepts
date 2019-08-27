import numpy as np
import cv2

def do_stuff(x):
    print(x)

# Create a black image, a window
img = np.zeros((300,512,3), np.uint8)
#creates a named window
cv2.cv2.namedWindow("image")

#bind the trackbar to our named window
cv2.cv2.createTrackbar("BlueTrackbar", "image", 0, 255, do_stuff)
cv2.cv2.createTrackbar("GreenTrackbar", "image", 0, 255, do_stuff)
cv2.cv2.createTrackbar("RedTrackbar", "image", 0, 255, do_stuff)

toggle_bgr = "0 : OFF\n 1 : ON"
cv2.cv2.createTrackbar(toggle_bgr, "image", 0, 1, do_stuff)

while(1):
    cv2.cv2.imshow("image",img)
   
    if cv2.cv2.waitKey(1) & 0xFF == 27:
        break

    blueValue = cv2.cv2.getTrackbarPos("BlueTrackbar", "image")
    greenValue = cv2.cv2.getTrackbarPos("GreenTrackbar", "image")
    redValue = cv2.cv2.getTrackbarPos("RedTrackbar", "image")
    switchValue = cv2.cv2.getTrackbarPos(toggle_bgr, "image")

    if switchValue == 0:
       img[:] = 0
    else:
       img[:] = [blueValue, greenValue, redValue]


cv2.cv2.destroyAllWindows()