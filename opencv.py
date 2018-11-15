#OpenCV

import cv2
import matplotlib.pyplot as plt
import numpy as np

##PART I

# #Load an color image in grayscale
# img=cv2.imread('_02_01.png',0)
# #Display an image using cv2
# # cv2.imshow('imgae',img)
# # #is a keyboard binging functions
# # cv2.waitKey(0)
# # #simply destroysallwindows
# # cv2.destroyAllWindows()
#
#
# #destroyAllWindows bases on conditions
# # k = cv2.waitKey(0)
# # if k == 27:         # wait for ESC key to exit
# #     cv2.destroyAllWindows()
# # elif k == ord('s'): # wait for 's' key to save and exit
# #     cv2.imwrite('messigray.png',img)
# #     cv2.destroyAllWindows()
#
# #show image using matplotlib
# plt.imshow(img,cmap='gray',interpolation='bicubic')
# # plt.xticks([0,442]),plt.yticks([0,250])
# plt.plot([50,100],[80,100],'c',linewidth=4)
# plt.show()
# cv2.imwrite("test.png",img)


##PART II

cap=cv2.VideoCapture(0)
while (True):
    # Capture frame-by-frame
    ret,frame = cap.read()
    #Our operations on the frame come here

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',frame)
    cv2.imshow('frame',gray)

    #Display the resulting frame
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
#When everthing done, release the capture
cap.release()
cv2.destroyAllWindows()


##PART III
