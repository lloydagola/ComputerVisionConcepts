import cv2
import numpy as np

def print_value(value):
    print(value)

video = cv2.cv2.VideoCapture(0)

cv2.cv2.namedWindow("Tracking")
cv2.cv2.createTrackbar("HueFloor", "Tracking", 0, 255, print_value)
cv2.cv2.createTrackbar("SaturationFloor", "Tracking", 0, 255, print_value)
cv2.cv2.createTrackbar("ValueFloor", "Tracking", 0, 255, print_value)
cv2.cv2.createTrackbar("HueCeiling", "Tracking", 255, 255, print_value)
cv2.cv2.createTrackbar("SaturationCeiling", "Tracking", 255, 255, print_value)
cv2.cv2.createTrackbar("ValueCeiling", "Tracking", 255, 255, print_value)

while True:
    _,frame = video.read()

    hsvImage = cv2.cv2.cvtColor(frame, cv2.cv2.COLOR_BGR2HSV)

    hue_floor = cv2.cv2.getTrackbarPos("HueFloor", "Tracking") 
    saturation_floor = cv2.cv2.getTrackbarPos("SaturationFloor", "Tracking")
    value_floor = cv2.cv2.getTrackbarPos("ValueFloor", "Tracking")

    hue_ceiling = cv2.cv2.getTrackbarPos("HueCeiling", "Tracking")
    saturation_ceiling = cv2.cv2.getTrackbarPos("SaturationCeiling", "Tracking")
    value_ceiling = cv2.cv2.getTrackbarPos("ValueCeiling", "Tracking")

    color_floor = np.array([hue_floor, saturation_floor, value_floor])
    color_ceiling = np.array([hue_ceiling, saturation_ceiling, value_ceiling])

    mask = cv2.cv2.inRange(hsvImage, color_floor, color_ceiling)

    result = cv2.cv2.bitwise_and(frame, frame, mask=mask)

    cv2.cv2.imshow("Colored balls", frame)
    cv2.cv2.imshow("Mask", mask)
    cv2.cv2.imshow("Result", result)

    if cv2.cv2.waitKey(1) & 0xFF == 27:
        break

video.release()
cv2.cv2.destroyAllWindows()