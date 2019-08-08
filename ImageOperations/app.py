import cv2

picture = cv2.cv2.imread("pexels.jpeg")

cv2.cv2.imshow("Result", picture)

if cv2.cv2.waitKey(0) & 0xFF == 27:
    cv2.cv2.destroyAllWindows()