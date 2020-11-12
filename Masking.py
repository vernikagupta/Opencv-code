# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 08:49:53 2020

@author: vernika
"""

'''Masking helps in focusing on area of interest in an image and mask the 
rest of the image.'''

 
import numpy as np
import cv2
import argparse


def show_img(img):
    cv2.imshow("canvas",img)
    cv2.waitKey(0)
    return

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "path to image")
args = vars(ap.parse_args())

load_image = cv2.imread(args["image"])
show_img(load_image)

centerX, centerY = load_image.shape[1]//2, load_image.shape[0]//2

'''first we create a rectangular black image of same shape as of original'''

mask = np.ones(load_image.shape[:2], dtype = 'uint8')
show_img(mask)

'''then we are ceating rectangle in the center of mask as we want to mask 
the center area of original image'''

cv2.rectangle(mask, (centerX-75,centerY-75),(centerX+75,centerY+75), 255, -1)
show_img(mask)
masked_img = cv2.bitwise_and(load_image, load_image, mask)
show_img(masked_img)


'''Suppose you want to create a white mask instead of black as we need in this case'''
mask = np.ones(load_image.shape[:2], dtype = 'uint8') * 255
show_img(mask)

'''create a circular mask'''

cv2.circle(mask, (centerX, centerY), 80, 0, -1 )
show_img(mask)
masked_img = cv2.bitwise_and(load_image, load_image, mask)
show_img(masked_img)

'''The cv2.bitwise_and function only examines pixels that are
“on” in the mask.'''