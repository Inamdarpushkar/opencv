#OpenCV

import cv2
import matplotlib.pyplot as plt
import numpy as np

##PART I

# #Load an color image in grayscale
#img=cv2.imread('_02_01.png',0)
img1=cv2.imread('_03_02.png',0)

print (img1.shape)
print(img1.size)
# print(img1.shape)
# print(img1.size)

# #Display an image using cv2
cv2.imshow('imgae',img1)
cv2.imshow('im',img1)
# # #is a keyboard binging functions
cv2.waitKey(0)
# # #simply destroysallwindows
cv2.destroyAllWindows()
