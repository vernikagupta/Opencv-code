# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 18:33:24 2020

@author: vernika
"""

'''Practically, this means that each pixel in the image is
mixed in with its surrounding pixel intensities. 
This “mixture” of pixels in a neighborhood becomes our blurred pixel.'''

'''Averaging means take an odd (k* k ) kernal, then intensity at the center 
is avergae of all the pixels below the kernal'''


import cv2
import argparse
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "path to image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

blurred = np.hstack([
        cv2.blur(image, (3, 3)),
        cv2.blur(image, (5, 5)),
        cv2.blur(image, (7, 7))])
cv2.imshow("Averaged", blurred)
cv2.waitKey(0)
        
'''--------------------------Gaussian Blurr---------------------------'''
'''Gaussian blurring is same as averaging but instead of taking simple
mean, we take weighted mean. Pixels that are close to the center contribute
more towards average and far away pixels less. In this way, picture will be
less blurr but more naturally blurr than Averaging'''

blurred = np.hstack([
        cv2.GaussianBlur(image, (3, 3), 0),
        cv2.GaussianBlur(image, (5, 5), 0),
        cv2.GaussianBlur(image, (7, 7), 0)])
cv2.imshow("GaussianBlur", blurred)
cv2.waitKey(0)

''' 0 is the standard deviation(sigma) in x direction. By giving zero, we are 
asking OpenCV to calculate it automatically.'''

'''--------------------Median Blurr---------------------------------'''
'''Median Blurring is used to to remove salt and pepper noise. It doesn't 
blurr the image like averaging or Gaussian blurr but it loose small details
in the image. Notice here, we are no longer creating a motion blurr or out of focus
effect but we are removing small details and noise.

Median blurr remove noise because center pixel is replaced by the 
median value which is also a part of image pixels. Averaging or gaussian blurr 
take mean of pixels which may or may not be part of original image'''
blurred = np.hstack([
        cv2.medianBlur(image, 3),
        cv2.medianBlur(image, 5),
        cv2.medianBlur(image, 7)])
cv2.imshow("medianBlur", blurred)
cv2.waitKey(0)

'''-----------------------Bilateral Blurring--------------------------'''
'''so far, we are trying to remove noise and details in the image but it has 
a disadvantage, that we loose edges also in the image which can be useful for 
object detection stuff. To preserve edges but still remove noise and details
we use Bilateral Blurring.'''

'''In Bilateral blurring, we make use of two Gaussian Distributions.
First gaussian function consider only those neighbour pixels that are 
close to the center pixel and second Gaussian function then models the pixel
intensity of neighbourhood ensuring that pixels having similar intensity
contribute in actual computation of blur'''

'''This way Bilateral blurring preserve edges while still removing noise
but downfall is this method is slow as compared to averaginf, Gaussian blurr
or median blurr'''


blurred = np.hstack([
        cv2.bilateralFilter(image, 5, 21, 21),
        cv2.bilateralFilter(image, 7, 31, 31),
        cv2.bilateralFilter(image, 9, 41, 41)])
cv2.imshow("bilateralFilter", blurred)
cv2.waitKey(0)

''' The first parameter we supply is the image we want to blur.
Then, we need to define the diameter of our pixel neighborhood. 
The third argument is our color σ. A larger value for color σ means that 
more colors in the neighborhood will be considered when computing the
blur. Finally, we need to supply the space σ. A
larger value of space σ means that pixels farther out from
the central pixel will influence the blurring calculation, 
provided that their colors are similar enough.'''