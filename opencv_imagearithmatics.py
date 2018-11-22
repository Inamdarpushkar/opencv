#OpenCV

import cv2
import matplotlib.pyplot as plt
import numpy as np

##PART I

# #Load an color image in grayscale

img1=cv2.imread('_01_02.png')
#img2=cv2.imread('_02_01.png')
img2=cv2.imread('t.png')
# add1=img1+img2
# add=cv2.add(img1,img2)
# subs=cv2.subtract(img1,img2)
# imgs1=img1/2
# imgs2=img2/2
#
# adds=cv2.add(imgs1,imgs2)
#
# # # #is a keyboard binging functions
# cv2.imshow('add1',add1)
# cv2.imshow('add',add)
# cv2.imshow('subs1',subs)
# cv2.imshow('subs',subs)
# cv2.imshow('im1',imgs1)
# cv2.imshow('im2',img2)


# weighted=cv2.addWeighted(img1,0.6,img2,0.4,0)
#
# cv2.imshow("weighted",weighted)

rows,cols,channels=img2.shape
roi=img1[0:rows,0:cols]
img2gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret,mask=cv2.threshold(img2gray,100,255,cv2.THRESH_BINARY_INV)

#cv2.imshow("mask",mask)











cv2.waitKey(0)
# # #simply destroysallwindows
cv2.destroyAllWindows()
