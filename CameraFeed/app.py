import cv2


camera_feed = cv2.cv2.VideoCapture(0)

while camera_feed.isOpened():
    frameIsAvailable, current_frame = camera_feed.read()

    if frameIsAvailable:
        grey_scale = cv2.cv2.cvtColor(current_frame, cv2.cv2.COLOR_BGR2GRAY)
        cv2.cv2.imshow("Camera feed", grey_scale)

        if cv2.cv2.waitKey(1) & 0xFF == 27:
            break

camera_feed.release()
cv2.cv2.destroyAllWindows()

