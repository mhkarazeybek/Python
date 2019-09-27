import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
while True:
    _, frame = cap.read()
    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    blurredFrame = cv.GaussianBlur(frame, (5, 5), 0)

    laplacian = cv.Laplacian(blurredFrame, cv.CV_64F)
    canny = cv.Canny(blurredFrame, 100, 150)

    cv.imshow("Frame", frame)
    cv.imshow("Laplacian", laplacian)
    cv.imshow("Canny", canny)

    key = cv.waitKey(1)
    if key ==27:
        break

cap.release()
cv.destroyAllWindows()
