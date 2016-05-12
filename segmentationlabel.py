# -*- coding: utf-8 -*-
"""
Created on Wed May  4 10:25:06 2016

@author: luiz
"""
from skimage import io,filters
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from skimage import data
from skimage.filters import threshold_otsu
from skimage.segmentation import clear_border
from skimage.measure import label
from skimage.morphology import closing, square
from skimage.measure import regionprops
from skimage.color import label2rgb


image = data.coins()[50:-50, 50:-50]

#im2 = np.zeros(image.shape)
#im3 = np.zeros(image.shape)
#im2 =  filters.median(image,np.ones((10,10)))
#im3 = (image/im2)*220
#im4 = np.zeros(image.shape)

#image = io.imread("coins.png")


# apply threshold
thresh = threshold_otsu(image)
bw = closing(image > thresh, square(3))

# remove artifacts connected to image border
cleared = bw.copy()
clear_border(cleared)

l,c=0,0

# label image regions
label_image = label(cleared)
image_label_overlay = label2rgb(label_image, image=image)

fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(10, 10))
ax.imshow(image_label_overlay)


for region in regionprops(label_image):

    # skip small images
    if region.area < 100:
        continue
    if l == 0:
        reset_region = region
 
    minr, minc, maxr, maxc = region.bbox
    rows = maxr - minr
    lins = maxc - minc
    
    if l*c < rows*lins:
        l=lins
        c=rows
        ponto = region
        

    # draw rectangle around segmented coins    
    rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
                              fill=False, edgecolor='blue', linewidth=2)
    ax.add_patch(rect)

#pinta retangulo vermelho na maior moeda
minr, minc, maxr, maxc = ponto.bbox
rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
                          fill=False, edgecolor='red', linewidth=2)
ax.add_patch(rect)

region = reset_region

### muda pra fundo preto as areas onde nao tem moeda
#for region in regionprops(label_image):
#    # skip small images
#    if region.area < 100:
#        continue
#    #verifica qual e a moeda mais clara
#    #ao final do for a maior media fica no c
#    im4[label_image == region.label] = image[label_image == region.label]
##    print(image[label_image] == region.label)
## 4r²R²/4r²R² = 1 quanto mais proximo mais redonda 4rA/p² p=2rR
#c = 0
#region = reset_region
#esse for verifica a regiao mais clara
for region in regionprops(label_image):
    # skip small images
    if region.area < 100:
        continue
    #verifica qual e a moeda mais clara
    #ao final do for a maior media fica no c
    x = image[label_image == region.label].mean()
    print(x)
    if c == 0:
        c = x
    if c < x:
        c = x

region = reset_region

#pinta a regiao mais clara de verde
for region in regionprops(label_image):
        # skip small images
    if region.area < 100:
        continue
#    print(region.label)
    if image[label_image == region.label].mean() == c:
        
        minr, minc, maxr, maxc = region.bbox
    #    l=maxr-minr
    #    c=maxc-minc
        #pinta retangulo vermelho na mas clara moeda
        minr, minc, maxr, maxc = region.bbox
        rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
                                  fill=False, edgecolor='green', linewidth=2)
        ax.add_patch(rect)
        
#linha,coluna = image.shape
#q=w=0

        
        
##print(label_image)
#for region in regionprops(label_image):
#    for q in range(linha):
#        for w in range(coluna):
#            print(image[label_image == region.label])
#            break
#        break

        
#plt.imshow(image,cmap="gray")

#plt.figure()
#plt.subplot(221)
#plt.imshow(im2, cmap="gray")
#plt.subplot(222)
#plt.imshow(im3, cmap="gray")
#plt.subplot(223)
#plt.imshow(im4, cmap="gray")
#plt.subplot(224)
plt.imshow(image, cmap="gray")
plt.show()