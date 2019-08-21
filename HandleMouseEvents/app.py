import numpy as np
import cv2

#events = [i for i in dir(cv2) if "EVENT" in i]
#print(events)

def click_event(event, x, y, flags, param):
    if event == cv2.cv2.EVENT_LBUTTONDOWN:
        print(x, " ", y)
        
        font = cv2.cv2.FONT_HERSHEY_SIMPLEX
        coordinates = str(x) + ", " + str(y)

        cv2.cv2.putText(img, coordinates, (x, y), font, 1, (255, 255, 0), 2)
        cv2.cv2.imshow("image", img)

    if event == cv2.cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]

        font = cv2.cv2.FONT_HERSHEY_SIMPLEX
        bgr_values = str(blue) + ", " + str(green) + ", " + str(red)

        cv2.cv2.putText(img, bgr_values, (x, y), font, 1, (0, 255, 255), 2)
        cv2.cv2.imshow("image", img)

img = cv2.cv2.imread("pexels.jpeg")
cv2.cv2.imshow("image", img)

cv2.cv2.setMouseCallback("image", click_event)

cv2.cv2.waitKey(0)
cv2.cv2.destroyAllWindows()