import numpy as np 
import matplotlib.pyplot as plt 
import cv2


img1=np.zeros(shape=[500,500,3],dtype=np.int32)
print(plt.imshow(img1))

rec=cv2.rectangle(img1,pt1=[250,30],pt2=[500,30],color=(0,0,255),thickness=2)
print(plt.imshow(img1))

cr=cv2.circle(img1,center=(20,20),radius=25,color=[254,0,0],thickness=3)
print(plt.imshow(img1))

li=cv2.line(img1,pt1=(0,0),pt2=(25,89),color=(255,255,255),thickness=5)
print(plt.imshow(img1))
