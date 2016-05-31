# -*- coding: utf-8 -*-
"""
Created on Wed May 18 10:34:17 2016

@author: luiz
"""
from skimage import io,color
import matplotlib.pyplot as plt
from skimage.segmentation import slic
import numpy as np
from sklearn.cluster import KMeans

im = io.imread("c001_01.png")

img = color.rgb2hsv(im)
segments = slic(img, n_segments=2)
w, h, d = img.shape
image_array = np.reshape(img, (w * h, d))

kmeans = KMeans(n_clusters=2).fit(image_array)
labels = kmeans.predict(image_array)
seg2 = np.reshape(labels, (w,h))

plt.figure()
plt.subplot(121)
plt.imshow(im)
plt.subplot(122)
plt.imshow(seg2, cmap="gray")
plt.show()