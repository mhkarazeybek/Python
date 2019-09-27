#mouse ile herhangi bir objenin üzerine tıklayıp hareket ettirebilirsiniz
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

#Create old frame
_, frame = cap.read()
oldGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Lucas kanade params
lkParams = dict(winSize=(15, 15),
                maxLevel=4,
                criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

# Mouse function
def selectPoint(event, x, y, flags, params):
    global point, pointSelected, oldPoints
    if event == cv2.EVENT_LBUTTONDOWN:
        point = (x, y)
        pointSelected = True
        oldPoints = np.array([[x, y]], dtype=np.float32)

cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame", selectPoint)

pointSelected = False
point = ()
oldPoints = np.array([[]])

while True:
    _, frame = cap.read()
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if pointSelected is True:
        cv2.circle(frame, point, 5, (0, 0, 255), 2)

        newPoints, status, error = cv2.calcOpticalFlowPyrLK(oldGray, grayFrame, oldPoints, None, **lkParams)
        oldGray = grayFrame.copy()
        oldPoints = newPoints

        x, y = newPoints.ravel()
        cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)


    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
