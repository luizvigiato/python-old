# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 15:21:00 2016

@author: luiz
"""

from skimage import io
import matplotlib.pyplot as plt
import numpy as np


def average(pixel):
    M = pixel.sum()/3
    M = int(M)
    return M
    

rgb = io.imread("lenna.jpg")

rows,cols,prof = rgb.shape

im = np.zeros((rows,cols))

for l in range(rows):
    for c in range(cols):
        gray = average(rgb[l,c,:])
        im[l,c] = gray 
        
plt.figure()
plt.subplot(121)
plt.imshow(rgb)
plt.subplot(122)
plt.imshow(im,cmap="gray") #R
plt.show()