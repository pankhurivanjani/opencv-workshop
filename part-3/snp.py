import numpy as np
import cv2

#In saltandpepper.png, there is salt and pepper noise

img = cv2.imread('saltandpepper.png',0)

# Use blurring to remove it!



cv2.imshow('img',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
