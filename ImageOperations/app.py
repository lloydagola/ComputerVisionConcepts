import cv2

picture = cv2.cv2.imread("pexels.jpeg")

print(picture.shape)    #returns a tuple of number of rows, columns and channels
print(picture.size)     #returns total number of pixels accessed
print(picture.dtype)    #returns Image datatype obtained


blue, green, red = cv2.cv2.split(picture)
picture = cv2.cv2.merge((blue, green, red))

cv2.cv2.imshow("Result", picture)

if cv2.cv2.waitKey(0) & 0xFF == 27:
    cv2.cv2.destroyAllWindows()