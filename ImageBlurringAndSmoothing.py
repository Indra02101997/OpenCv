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
    kernel=np.ones((5,5),np.float32)/25
    mean=cv2.filter2D(res,-1,kernel)
    gauss=cv2.GaussianBlur(res,(5,5),0)
    median=cv2.medianBlur(res,5)
    bilateral=cv2.bilateralFilter(res,5,75,75)
    cv2.imshow('res',res)
    cv2.imshow('mean',mean)
    cv2.imshow('gauss',gauss)
    cv2.imshow('meadian',median)
    cv2.imshow('bilateral',bilateral)
    if(cv2.waitKey(0)&0xFF==ord('q')):
        break
cv2.destroyAllWindows()
cap.release()
