# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 13:43:59 2020

@author: vernika
"""

'''Thresholding means convert image into binary. We have a gray scale image 
and we set a threshold p, all pixel values below p will be zero (black) and otherwise 
one (white). 

we use thresholding to focus on objects or particular area of interest'''


#------------------simple thresholding--------------------------------------


import cv2
import argparse

def show_img(w_name,img):
    cv2.imshow(w_name, img)
    cv2.waitKey(0)
    return

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "path to image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5, 5), 0)
#Gaussian blurring we apply to remove higher freqency 
#edges in the image

(T, thresh) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY) 
# threshold_value - 155
# max_pixel_value - 255
# any pixel value above 155 will be 255
show_img("simple_thresh",thresh)
(T, threshInv) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY_INV)
show_img("invese_thresh",threshInv)


#---------------------Adaptive Thresholdng-------------------------------
'''when image pixel intensity exhibit a lot of range then difficult to select
one threshold that works for all pixels. so, we use adaptive which makes use of
small region of neighbour pixels and decide threshold for each neighbour pixel'''

thresh = cv2.adaptiveThreshold(blurred, 255,cv2.ADAPTIVE_THRESH_MEAN_C, \
                               cv2.THRESH_BINARY_INV, 11, 4)
show_img("Adaptive mean theshold",thresh)

# 11 represent neighbour size (11*11 region of image to comute mean)
# C is a no we subtract from out mean to fine tune the thresholdings

thresh = cv2.adaptiveThreshold(blurred, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                               cv2.THRESH_BINARY_INV, 15, 3)

show_img("Adaptive gaussian theshold",thresh)

# Gaussian is weighted mean thresholding
# 15*15 neighbour size and 3 as no for subtracting from threshold value for fine tuning
#In general, choosing between mean adaptive thresholding and 
#Gaussian adaptive thresholding requires a few experiments on your end.

#-------------------------------OSTU Thresholding------------------------------
'''Ostu method assumes there are two peaks in pixels intensity  of image.
Method finds an optimal value of pixel intensity and try to separate the 
two peaks thus thresholding. we use mahotas library for it and can use opencv as well'''

import mahotas
# pass the gaussian blurred image 
T = mahotas.thresholding.otsu(blurred)
print("Otsu’s threshold: {}".format(T))
thresh = image.copy()   # copy of grayscale image
thresh[thresh > T] = 255
thresh[thresh < 255] = 0
thresh = cv2.bitwise_not(thresh) # binary inverse thresholding


#---------------Riddler-Calvard------------------------------------------------
T = mahotas.thresholding.rc(blurred)
print("Riddler-Calvard: {}".format(T))
thresh = image.copy()
thresh[thresh > T] = 255
thresh[thresh < 255] = 0
thresh = cv2.bitwise_not(thresh)
cv2.imshow("Riddler-Calvard", thresh)
cv2.waitKey(0)
