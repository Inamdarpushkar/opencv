#OpenCV

import cv2
import matplotlib.pyplot as plt
import numpy as np

##PART I

# #Load an color image in grayscale
# img=cv2.imread('_02_01.png',0)
##
# print (img.shape)
# print(img.size)
# # #Display an image using cv2
# cv2.imshow('imgae',img)
# # # #is a keyboard binging functions
# cv2.waitKey(0)
# # # #simply destroysallwindows
# cv2.destroyAllWindows()
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
#
# cap=cv2.VideoCapture(0)
# fourcc=cv2.VideoWriter_fourcc(*'xvid')
# out=cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))



# while (True):
#     # Capture frame-by-frame
#     ret,frame = cap.read()
#     #Our operations on the frame come here
#
#     gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#     out.write(frame)
#     cv2.imshow('frame',gray)
#     cv2.imshow('framgcolor',frame)
#
#     #Display the resulting frame
#     if cv2.waitKey(1) & 0xFF==ord('q'):
#         break
# #When everthing done, release the capture
# cap.release()
# out.release()
# cv2.destroyAllWindows()


##PART III
# #adding different things on the image
# img=cv2.imread("_02_01.png",cv2.IMREAD_COLOR)
#
# #adding line,rectangle,circle,poygon
# cv2.line(img,(0,0),(150,150),(255,255,255),15)
# cv2.rectangle(img,(15,25),(200,150),(0,255,0),5)
# cv2.circle(img,(100,63),55,(0,255),-1)
#
# pts=np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
# #pts=pts.reshape((-1,1,2))
# cv2.polylines(img,[pts],True,(0,255,255),5)
#
# #adding text to the image
# font=cv2.FONT_HERSHEY_SIMPLEX
# cv2.putText(img,'Test',(0,130),font,0.5,(200,255,255),5,cv2.LINE_AA)
#
# cv2.imshow('img',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# IV
# img=cv2.imread('_02_01.png',cv2.IMREAD_COLOR)
# # img[55,55]=[255,255,255]
# # print(img[55,55])
#
#
# img[100:150,100:150]=[255,255,255]
#
# cv2.imshow('img',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
