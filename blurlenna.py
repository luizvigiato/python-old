# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 10:23:30 2016

@author: luiz
"""

from skimage import io
import matplotlib.pyplot as plt
import numpy as np

im = io.imread("talita.jpg")

print(im.shape)
lin,col,prof = im.shape
#cria uma matriz cheias de zeros pra depois poder sem preencida
#com a im alterada
img2 =np.zeros((lin,col,prof),'uint8')

for l in range(5,lin-5):
    for c in range(5,col-5):
        #funcao .mean() pra fazer a media de valores
        #OBS! funcao orientada! por isso fica assim
        R= im[l-5:l+6,c-5:c+6,0].mean()
        G= im[l-5:l+6,c-5:c+6,1].mean()
        B= im[l-5:l+6,c-5:c+6,2].mean()        
        img2[l,c,:] = R,G,B

plt.figure()
plt.subplot(121)
plt.imshow(im)
plt.subplot(122)
plt.imshow(img2)
plt.show()

        