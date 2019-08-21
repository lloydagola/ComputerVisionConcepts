import cv2

cameraFeed = cv2.cv2.VideoCapture(0)

cameraFeed.set(cv2.cv2.CAP_PROP_FRAME_WIDTH, 1280)
cameraFeed.set(cv2.cv2.CAP_PROP_FRAME_HEIGHT, 720)
print(cameraFeed.get(cv2.cv2.CAP_PROP_FRAME_WIDTH))
print(cameraFeed.get(cv2.cv2.CAP_PROP_FRAME_HEIGHT))

while(cameraFeed.isOpened()):
    frame_is_available, currentFrame = cameraFeed.read()

    if frame_is_available:

        cv2.cv2.imshow("Camera Feed", currentFrame)

        if(cv2.cv2.waitKey(1) & 0XFF == 27):
            break
    
    else:
        break
  
cameraFeed.release()
cv2.cv2.destroyAllWindows()
