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
cv2.imshow("threshold", thresh)
cv2.waitKey(0)
(T, threshInv) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Inverse_threshold", threshInv)
cv2.waitKey(0)





