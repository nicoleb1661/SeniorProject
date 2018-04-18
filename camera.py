import numpy as np
import cv2
import imutils

cap = cv2.VideoCapture(0)


    #Capture frame by frame
   # camera = cv2.VideoCapture(1)

   # (grabbed, frame) = camera.read()
while True:
    ret, frame = cap.read()

    (grabbed, frame) = cap.read()
    text = "HELLO"

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #display results in gray scale
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    #release everything/closes windows
cap.release();
cv2.destryAllWindows()
