# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 11:06:26 2016

@author: luiz
"""

from skimage import io
import matplotlib.pyplot as plt
import numpy as np

im = io.imread("talita.jpg")

print(im.shape)
lin,col,prof = im.shape
img2 =np.zeros((lin,col,prof),'uint8')
img3 =np.zeros((lin,col,prof),'uint8')

filtro=np.ones((3,3))
filtro=filtro/9

for l in range(1,lin-1):
    for c in range(1,col-1):
        R= np.multiply(im[l-1:l+2,c-1:c+2,0], filtro).sum()
        G= np.multiply(im[l-1:l+2,c-1:c+2,1], filtro).sum()
        B= np.multiply(im[l-1:l+2,c-1:c+2,2], filtro).sum()   
        img2[l,c,:] = R,G,B
        
realce = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
for l in range(1,lin-1):
    for c in range(1,col-1):
        R= np.multiply(img2[l-1:l+2,c-1:c+2,0], realce).sum()
        G= np.multiply(img2[l-1:l+2,c-1:c+2,1], realce).sum()
        B= np.multiply(img2[l-1:l+2,c-1:c+2,2], realce).sum()  
        if R > 255:
            R=255
        if R < 0:
            R=0
        if G > 255:
            G=255
        if G < 0:
            G=0
        if B > 255:
            B=255
        if B < 0:
            B=0
        img3[l,c,:] = R,G,B
        
plt.figure()
plt.subplot(131)
plt.imshow(im)
plt.subplot(132)
plt.imshow(img2)
plt.subplot(133)
plt.imshow(img3)
plt.show()