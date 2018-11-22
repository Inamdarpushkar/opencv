import cv2
import numpy as np

#importing an image
img=cv2.imread('bookpage.jpg')

#Setting a threshold of 12
# as the image has low light threshold value is low. So any value above 12 is converted to hight
# DM value, 255 is max DM value.
retval,threshold=cv2.threshold(img,12,255,cv2.THRESH_BINARY)

#converting to grayscale image
grayscaled=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval,threshold2=cv2.threshold(grayscaled,12,255,cv2.THRESH_BINARY)
#displaying images
cv2.imshow('original',img)
cv2.imshow('threshold',threshold)
cv2.imshow('threshold2',threshold2)

#keyboard connection press any key to destroyAllWindows
cv2.waitKey(0)
cv2.destroysallwindows()
