import numpy as np
import cv2

cap=cv2.VideoCapture(0)
while True :
    _,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower=np.array([100,100,50])
    upper=np.array([180,255,150])
    mask=cv2.inRange(hsv,lower,upper)
    res=cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    if(cv2.waitKey(0) & 0xFF==ord('q')):
        break

cv2.destroyAllWindows()
cap.release()
