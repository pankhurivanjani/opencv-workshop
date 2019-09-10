import numpy as np
import cv2

#A camera installed at our self-driving car captures a frame given in frame.jpg

img = cv2.imread('frame.jpg')

#Our detector has detected a traffic light signal in this frame
#Rectangle surrounding these are given in the following list listing top-left and bottom-right coordinates.

lights = [  [(22,105),(72,128)],
            [(206,116),(256,136)],
            [(515,183),(537,232)]   ]

#Write a color recognition algorithm to identify 
# whether the detected traffic lights have signal of red or green.
#Upper and lower HSV value ranges for red and green are given in the following list.

lower_green = np.array([30,100,120])
upper_green = np.array([120,255,255])
lower_red = np.array([130,100,120])
upper_red = np.array([180,255,255])


    
cv2.imshow('img',img)

cv2.waitKey(0)
cv2.destroyAllWindows()