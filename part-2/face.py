import numpy as np
import cv2

#Read image boroque.jpg



#Using our face detector, we have detected a face in this image
#A rectangle covering this face has top-left coordinates (x,y) and width and height w and h.

x,y,w,h = (116,42,62,62)

# Using OpenCV draw a rectangle around this face using given data and show this new image.



cv2.waitKey(0)
cv2.destroyAllWindows()
