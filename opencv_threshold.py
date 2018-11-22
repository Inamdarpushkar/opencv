import cv2
import numpy as np

#importing an image
img=cv2.imread('bookpage.jpg')

#Setting a threshold of 12 (or some other value based on the brightness)
# as the image has low light threshold value is low. So any value above 12 is converted to hight
# DM value, 255 is max DM value.
retval,threshold=cv2.threshold(img,12,255,cv2.THRESH_BINARY)

#converting to grayscale image
grayscaled=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval,threshold2=cv2.threshold(grayscaled,12,255,cv2.THRESH_BINARY)

#adaptive threshold (adjust threshold based on the global DM values)
gaus=cv2.adaptiveThreshold(grayscaled,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,155,1)
#
retval,otsu=cv2.threshold(grayscaled,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

#displaying images
cv2.imshow('original',img)
cv2.imshow('threshold',threshold)
cv2.imshow('threshold2',threshold2)
cv2.imshow('Gaussian',gaus)
cv2.imshow('otsu',otsu)
#keyboard connection press any key to destroyAllWindows
cv2.waitKey(0)
cv2.destroysallwindows()
