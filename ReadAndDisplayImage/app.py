import cv2

#read an image file
input_picture = cv2.cv2.imread("pexels.jpeg")

#show the image in a new window named "Result"
cv2.cv2.imshow("Result", input_picture)

#close if the user clicks the escape key
if cv2.cv2.waitKey(0) & 0xFF == 27:
    cv2.cv2.destroyAllWindows()

