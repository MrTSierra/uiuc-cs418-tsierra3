# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 22:25:39 2021

@author: Trinidad
"""
import numpy as np
import cv2
import copy

im_2 = cv2.imread('illinois512_bump_input.png', cv2.IMREAD_COLOR)

print(type(im_2))

print(im_2.shape)

print(im_2.dtype)

"""
im_2 = im

im_2[:, :, (0,1)] = 0

cv2.imwrite('illinois512_bump_r.png', im_2)"""

im = im_2.astype(np.int16)

print(type(im))

print(im.shape)

print(im.dtype)

bump = copy.deepcopy(im_2)

img_x=512 #512
img_y=512

for i in range(img_x):
    for j in range(img_y):
        if(i==(img_x-1) and j==(img_y-1)):
           bump[i,j,0] = abs(im[0,0,2]-im[i,j,2])
           bump[i,j,1] = abs(im[0,0,2]-im[i,j,2])
           ##print("end of i:",i," j:",j)
        elif(i==(img_x-1)):
            bump[i,j,0] = abs(im[i,j+1,2]-im[i,j,2])
            bump[i,j,1] = abs(im[0,j,2]-im[i,j,2])
            #print("end of i:",i)
        elif(j==(img_y-1)):
            bump[i,j,0] = abs(im[i,0,2]-im[i,j,2])
            bump[i,j,1] = abs(im[i+1,j,2]-im[i,j,2])
            ##print("end of j:",j)
        else:
            bump[i,j,0] = abs(im[i,j+1,2]-im[i,j,2])
            bump[i,j,1] = abs(im[i+1,j,2]-im[i,j,2])
            if(0 and ((im[i,j+1,2]<im[i,j,2]) or (im[i+1,j,2]<im[i,j,2]))):
                print("i",i,"j",j,"abs(im[i,j+1,2]-im[i,j,2])", abs(im[i,j+1,2]-im[i,j,2]), "im[i,j+1,2]",im[i,j+1,2], "-im[i,j,2]",-im[i,j,2], "im[i,j,2]",im[i,j,2],"bump[i,j,0]", bump[i,j,0])
                print("i",i,"j",j,"abs(im[i+1,j,2]-im[i,j,2])", abs(im[i+1,j,2]-im[i,j,2]), "im[i+1,j,2]",im[i+1,j,2], "-im[i,j,2]",-im[i,j,2], "im[i,j,2]",im[i,j,2],"bump[i,j,1]", bump[i,j,1])
            
            
cv2.imwrite('illinois512_bump.png', bump)
