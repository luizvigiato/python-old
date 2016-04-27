# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 10:29:49 2016

@author: luiz
"""

from skimage import io,filters
import matplotlib.pyplot as plt
import numpy as np

im = io.imread("page.png")

print(im.shape)
img2 = np.zeros(im.shape)
img3 = np.zeros(im.shape)

#rows,cols=im.shape
#filtro = np.zeros((rows,1))
#print(filtro.shape)
#M = 0

#for c in range(cols):
#    M = M + im[:,c].sum()
#    M = M/rows
#    img2[:,c]=M
     
        
rows,cols = im.shape

img2 = filters.median(im,np.ones((15,15)))

img3 = (im/img2)*220

img4 = np.zeros(im.shape)

t = filters.threshold_otsu(im)

img4[img3<t] = 1


plt.figure()
plt.subplot(121)
plt.imshow(im, cmap="gray")
plt.subplot(122)
plt.imshow(img2, cmap="gray") #R
plt.show()
