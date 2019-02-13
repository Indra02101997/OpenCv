import numpy as np
import cv2

cap=cv2.VideoCapture(0)
while True:
    _,frame=cap.read()
    laplace=cv2.Laplacian(frame,cv2.CV_64F)
    sobelx=cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=3)
    sobely=cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=3)
    canny=cv2.Canny(frame,100,200)
    cv2.imshow('frame',frame)
    cv2.imshow('laplace',laplace)
    cv2.imshow('sobelx',sobelx)
    cv2.imshow('sobely',sobely)
    cv2.imshow('canny',canny)
    if(cv2.waitKey(0)&0xFF==ord('q')):
        break
cv2.destroyAllWindows()
cap.release()
