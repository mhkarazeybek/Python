import cv2
image = cv2.imread("../images/opencv.png")
grayImage=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

cv2.imshow("Gray OpenCV",grayImage)
cv2.imshow("Open CV", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
#cv2.imwrite("grayImage.jpg",grayImage)