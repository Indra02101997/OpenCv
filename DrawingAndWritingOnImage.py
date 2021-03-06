import numpy as np
import cv2

img =cv2.imread('block1.jpg',1)

cv2.line(img, (0,0), (350,50), (255,0,0), 20)

cv2.rectangle(img, (10,30), (200,100), (0,255,0), 5)

cv2.circle(img,(150,100), 45 , (0,0,255) ,-1)

pts=np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)

cv2.polylines(img, [pts], True , (0,255,255) ,5)

font=cv2.FONT_HERSHEY_SIMPLEX

cv2.putText(img, 'OpenCV!!', (0,20) ,font ,3, (0,0,0) ,2 ,cv2.LINE_AA)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
