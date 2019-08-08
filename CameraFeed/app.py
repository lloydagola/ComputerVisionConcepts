import cv2


camera_feed = cv2.cv2.VideoCapture(0)

while camera_feed.isOpened():
    frameIsAvailable, current_frame = camera_feed.read()

    if frameIsAvailable:
        cv2.cv2.imshow("Camera feed", current_frame)

        if cv2.cv2.waitKey(1) & 0xFF == 27:
            break

camera_feed.release()
cv2.cv2.destroyAllWindows()

