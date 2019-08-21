import cv2
import datetime

camera_feed = cv2.cv2.VideoCapture(0)

while(camera_feed.isOpened()):
    frameIsAvailable, currentFrame = camera_feed.read()

    if frameIsAvailable:

        font = cv2.cv2.FONT_HERSHEY_SIMPLEX
        date_and_time = str(datetime.datetime.now())

        currentFrame = cv2.cv2.putText(currentFrame, date_and_time, (10,50), font, 1, (0,255,255), 2, cv2.cv2.LINE_AA)

        cv2.cv2.imshow("Camera feed", currentFrame)

        if cv2.cv2.waitKey(1) & 0xFF == 27:
            break

    else:
        break

camera_feed.release()
cv2.cv2.destroyAllWindows()