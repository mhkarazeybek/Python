import cv2
import numpy as np
cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture("opencv.mp4")

fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("flippedOpenCVVideo.avi", fourcc, 25, (640, 360))

while True:
    ret,frame = cap.read()
    print(frame.shape)
    frame2 = cv2.flip(frame,1)
    #graySCale =cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #cv2.imshow("gray Scale", graySCale)
    cv2.imshow("flipping", frame2)
    cv2.imshow("frame", frame)
    #out.write(frame2)
    key = cv2.waitKey(30)
    if key == 27:
        break
out.release()
cap.release()
cv2.destroyAllWindows()