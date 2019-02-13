import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('GrabCutImage1.jpg')

mask=np.zeros(img.shape[:2],np.uint8)

bgdmodel=np.zeros((1,65),np.float64)
fgdmodel=np.zeros((1,65),np.float64)

rect=(161,85,147,180)

cv2.grabCut(img,mask,rect,bgdmodel,fgdmodel,5,cv2.GC_INIT_WITH_RECT)

mask2=np.where((mask==0)|(mask==2),0,1).astype('uint8')

res=cv2.bitwise_and(img,img,mask=mask2)
cv2.imshow('res',res)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
