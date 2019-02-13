import numpy as np
import cv2
import matplotlib.pyplot as plt

img=cv2.imread('block2.jpg',1)

cv2.imshow('image',img)

#plt.imshow(img,cmap='gray',interpolation='bicubic')
#plt.plot([200,100],[50,100], 'c', linewidth=5)
#plt.show()

cv2.waitKey(0)
cv2.imwrite('opencvimage1.png',img)
cv2.destroyAllWindows()
