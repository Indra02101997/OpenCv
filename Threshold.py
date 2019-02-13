import numpy as np
import cv2

img=cv2.imread('bookpage.jpg')

ret,threshold=cv2.threshold(img,12,255,cv2.THRESH_BINARY)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret1,threshold1=cv2.threshold(gray,12,255,cv2.THRESH_BINARY)
gauss=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,3)
ret1,otsu=cv2.threshold(gray,11,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow('threshold1',threshold)
cv2.imshow('threshold2',threshold1)
cv2.imshow('gauss',gauss)
cv2.imshow('otsu',otsu)
cv2.waitKey(0)
cv2.destroyAllWindows()
