import cv2
import numpy as np 

img = np.zeros([512, 512, 3], np.uint8)

img = cv2.cv2.line(img, (0,0), (0,255), (0, 0, 255), 5)
img = cv2.cv2.rectangle(img, (384, 0), (510, 128), (0,0,255), 5)
img = cv2.cv2.circle(img, (447, 63), 63, (0, 255, 0), -1)

font = cv2.cv2.FONT_HERSHEY_SIMPLEX
img = cv2.cv2.putText(img, "Random Text", (10,500), font, 4, (255,255,255), 10, cv2.LINE_AA)

img = cv2.cv2.rectangle(img, (384, 300), (510, 428), (0,0,255), -1)

cv2.cv2.imshow("Result", img)

key = cv2.cv2.waitKey(0) & 0xFF
if(key == 27) :
    cv2.cv2.destroyAllWindows()