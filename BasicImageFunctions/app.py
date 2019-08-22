import cv2
img = cv2.cv2.imread("Pexels.jpeg")

print(img.shape)
print(img.size)
print(img.dtype)

b,g,r = cv2.cv2.split(img)
img = cv2.cv2.merge((b,g,r))

cv2.cv2.imshow("image", img)
cv2.cv2.waitKey(0)
cv2.cv2.destroyAllWindows()