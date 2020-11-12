# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 13:08:19 2020

@author: vernika
"""

from __future__ import print_function
import cv2
import argparse


def show_img(img):
    cv2.imshow("canvas",img)
    cv2.waitKey(0)
    return

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "path to image")
args = vars(ap.parse_args())
print(args)

load_image = cv2.imread(args["image"])

def flip_img(img, alignment = None):
    if alignment == 1:       # horizontal flip
        flipped = cv2.flip(img, 1)
    elif alignment == 0:         # Vertical flip
        flipped = cv2.flip(img, 0)
    elif alignment == -1:         # horizontal and vertical flip
        flipped = cv2.flip(img, -1)        
    return flipped

def crop_img(img, ystart, yend, xstart, xend):
    cropped_img = img[ystart:yend, xstart:xend]
    return cropped_img
    
        