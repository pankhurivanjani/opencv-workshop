import numpy as np
import cv2

img = cv2.imread('c.png')
depth = cv2.imread('d.png',0)

blur = cv2.GaussianBlur(img,(35,35),0)

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if depth[i,j]<170:
            img[i,j,:]=blur[i,j,:]

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
