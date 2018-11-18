#OpenCV

import cv2
import matplotlib.pyplot as plt
import numpy as np

##PART I

# #Load an color image in grayscale
img=cv2.imread('_02_01.png',0)

print (img.shape)
print(img.size)
# #Display an image using cv2
cv2.imshow('imgae',img)
# # #is a keyboard binging functions
cv2.waitKey(0)
# # #simply destroysallwindows
cv2.destroyAllWindows()
