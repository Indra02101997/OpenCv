import numpy as np
import cv2

cap=cv2.VideoCapture(0)
while True:
    _,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower=np.array([100,100,50])
    upper=np.array([180,255,150])
    mask=cv2.inRange(hsv,lower,upper)
    res=cv2.bitwise_and(frame,frame,mask=mask)
    kernel=np.ones((5,5),np.float32)
    erosion=cv2.erode(mask,kernel,iterations=1)
    dilation=cv2.dilate(mask,kernel,iterations=1)
    opening=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
    close=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)
    cv2.imshow('frame',frame)
    cv2.imshow('res',res)
    cv2.imshow('erosion',erosion)
    cv2.imshow('dilation',dilation)
    cv2.imshow('opening',opening)
    cv2.imshow('close',close)
    if(cv2.waitKey(0)&0xFF==ord('q')):
        break
cv2.destroyAllWindows()
cap.release()
