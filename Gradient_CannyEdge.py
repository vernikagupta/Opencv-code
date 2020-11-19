# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 18:19:36 2020

@author: vernika
"""

'''Edge means when there is a high change in brightness of pixel intensity,
we say there is an edge. To compute edge, we use gradients. There are two 
Laplacian gradient and Sobel gradient. This is a multi step process.
we first blurr the gray image, then apply gradient calculation on image to find
Edge like regions. Then we do non max suppression and hystersis thresholding.'''

'''As thresholding is used to segment foreground and background of image.
Edge detection is used to outline the objects in image'''

import cv2
import argparse
import numpy as np

def show_img(w_name,img):
    cv2.imshow(w_name, img)
    cv2.waitKey(0)
    return

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "path to image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#--------------------Laplacian Gradient calculation--------------------------
lap = cv2.Laplacian(image, cv2.CV_64F) # cv2.CV_64F for output image data type
lap = np.uint8(np.absolute(lap))
show_img("laplacian",lap)

'''Always use floating data type for output image otherwise you will miss
some black to white edges. We know 8 bit unsigned integers doesn't represent
negative numbers as OpenCV clip the no below 0 and above 255. lly, numpy
use modulus operations to perform mathematics on images. Therefore use
64 bit floating point to get all edge like regions'''

#------------------Sobel operator-----------------------------------------
sobelX = cv2.Sobel(image, cv2.CV_64F, 1, 0)  # vertical edges like regions
sobelY = cv2.Sobel(image, cv2.CV_64F, 0, 1)  # horizontal edges like regions
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))
sobelCombined = cv2.bitwise_or(sobelX, sobelY)
show_img("Sobel X", sobelX)
show_img("Sobel Y", sobelY)
show_img("sobelCombined", sobelCombined)

'''last two arguments (1,0) represent the order of derivatives in 
X and Y direction'''

#---------------Canny edge detector---------------------------------------
'''It involves blurring the image to remove noise then sobel gradient calculation
to find edges like region in X and Y direction. Then supressing edges and
finally hystersis thresholding stage that determines if a pixel is edge like
or not.'''

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.GaussianBlur(image, (5, 5), 0)
canny = cv2.Canny(image, 30, 150)
show_img("Canny",canny)

''' first argument is blurred image and other two arguments are threshold1
and threshold2. any pixel below threshold1 is considered not edge and any pixel
above threshold2 is considered an edge. Pixel values between threshold1
and threshold2 are classified as edge or not edge based on how they are
"Connected".. In this case,
any gradient values below 30 are considered non-edges whereas
any values above 150 are considered edges.'''