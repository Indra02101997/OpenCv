import cv2
import numpy as np

img_bgr=cv2.imread('Template.jpg')
img_gray=cv2.cvtColor(img_bgr,cv2.COLOR_BGR2GRAY)

template=cv2.imread('MatchTemplate.jpg',0)
w,h=template.shape[::-1]
res=cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)

thres=0.8
pts=np.where(res>=thres)

for p in zip(*pts[::-1]):
    cv2.rectangle(img_bgr,p,(p[0]+w,p[1]+h),(0,255,255),2)
#arr=np.array(res)
#print(arr)

cv2.imshow('detected', img_bgr)
cv2.imshow('res',res)
cv2.waitKey(0)
cv2.destroyAllWindows()

