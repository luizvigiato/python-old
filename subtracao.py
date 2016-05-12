# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 10:29:49 2016

@author: luiz
"""

from skimage import io,filters
import matplotlib.pyplot as plt
import numpy as np

#def quicksort(v):
#    if len(v) <= 1:
#        return v # uma lista vazia ou com 1 elemento ja esta ordenada
#    less, equal, greater = [], [], [] # cria as sublistas dos maiores, menores e iguais ao pivo
#    pivot = v[0] # escolhe o pivo. neste caso, o primeiro elemento da lista
#    for x in v:
## adiciona o elemento x a lista correspondeste
#        if x < pivot:
#            less.append(x)
#        elif x == pivot:
#            equal.append(x)
#        else:
#            greater.append(x)
#    return quicksort(less) + equal + quicksort(greater) # concatena e retorna recursivamente
## .. as listas ordenadas


im = io.imread("page.png")

print(im.shape)
img2 = np.zeros(im.shape)
img3 = np.zeros(im.shape)

#rows,cols=im.shape
#filtro = np.zeros((rows,1))
#print(filtro.shape)
#M = 0
#M = quicksort(im[:,0])
#print(M)
#print(M[95])
#
#for c in range(cols):
#    M = quicksort(im[:,c])
#    if rows%2 != 0:
#        M = int(M[int(rows/2)]) + int(M[int(rows/2)+1])
#        M = int(M/2)
#    else:
#        M = M[rows/2]
#    img2[:,c]=M
     
        

img2 = filters.median(im,np.ones((15,15)))

img3 = (im/img2)*220

img4 = np.zeros(im.shape)

t = filters.threshold_otsu(im)

img4[img3<t] = 1


plt.figure()
plt.subplot(221)
plt.imshow(im, cmap="gray")
plt.subplot(222)
plt.imshow(img2, cmap="gray")
plt.subplot(223)
plt.imshow(img3, cmap="gray")
plt.subplot(224)
plt.imshow(img4, cmap="gray")
plt.show()
