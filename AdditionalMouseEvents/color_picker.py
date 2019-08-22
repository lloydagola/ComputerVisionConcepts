import numpy as np
import cv2

#events = [i for i in dir(cv2) if "EVENT" in i]
#print(events)

def click_event(event, x, y, flags, param):
    if event == cv2.cv2.EVENT_LBUTTONDOWN:
        #get the blue at the x,y coordinate and index 0 (b, g, r)
        blue = img[x, y, 0]
        green = img[x, y, 1]
        red = img[x, y, 2]

        cv2.cv2.circle(img, (x, y), 3, (0,0,255), -1)
        newColorWindow = np.zeros((512, 512, 3), np.uint8)

        newColorWindow[:] = [blue, green, red]
         
        cv2.cv2.imshow("Selected color", newColorWindow)

    
img = np.zeros((512, 512, 3), np.uint8)


cv2.cv2.imshow("image", img)

points = []

cv2.cv2.setMouseCallback("image", click_event)

cv2.cv2.waitKey(0)
cv2.cv2.destroyAllWindows()