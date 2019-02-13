import numpy as np
import cv2

img=cv2.imread('block2.jpg',1)

img[100,100]=[0,0,0];

print(img[100,100])

img[100:150,100:150]=[0,0,0]

face=img[40:100,50:100]
face=[255,255,255]
img[0:60,0:50]=face

cv2.imshow('image',img)

cv2.waitKey(0)

cv2.destroyAllWindows()
