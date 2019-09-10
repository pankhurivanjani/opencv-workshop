import numpy as np
import cv2

#Read image board.jpg



#Using our detector, we have detected the corner points given in the list
#[top-left , top-right , bottom-left , bottom-right].

corners = [ (38,75),
            (306,28),
            (90,288),
            (417,160) ]

#Using Affine Transformation, generate a top view of this board



cv2.imshow('input',img)
cv2.imshow('output',dst)

cv2.waitKey(0)
cv2.destroyAllWindows()