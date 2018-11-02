import cv2
import matplotlib.pyplot as plt
import numpy

img=cv2.imread('watch.jpg',cv2.IMREAD_GRAYSCALE)

#IMREAD_COLOR
#IMREAD_UNCHANGED =-1
#cv2.imshow('imgae',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
#plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.plot([200,300,400],[100,200,300],'c', linewidth=5)
plt.show()
