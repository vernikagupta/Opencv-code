# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 16:55:55 2020

@author: vernika
"""

'''Histogram equalization improves the contrast of an image
by “stretching” the distribution of pixels. Consider a histogram 
with a large peak at the center of it. Applying histogram equalization will 
stretch the peak out towards the corner of the image, thus improving the
global contrast of the image. Histogram equalization is applied to grayscale
images.
This method is useful when an image contains foregrounds and backgrounds 
that are both dark or both light. It tends to produce unrealistic effects
in photographs; however, it is normally useful when enhancing the contrast
of medical or satellite images.'''


import cv2
import argparse
import numpy as np

def show_img(img):
    cv2.imshow("canvas",img)
    cv2.waitKey(0)
    return

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "path to image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
eq = cv2.equalizeHist(image)
cv2.imshow("Histogram Equalization", np.hstack([image, eq]))
cv2.waitKey(0)