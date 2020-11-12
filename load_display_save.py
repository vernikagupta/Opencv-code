# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from __future__ import print_function
import cv2
import argparse


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "path to image")
args = vars(ap.parse_args())
print(args)

load_image = cv2.imread(args["image"])
print("width of image is: {} ".format(load_image.shape[1]))
print("height of image is: {} ".format(load_image.shape[0]))
print("channels of image is: {} ".format(load_image.shape[2]))


cv2.imshow("image", load_image)
cv2.waitKey(0)

#cv2.imwrite("path to the image", image)


# if you want to convert image into jpg, just load in png format in opencv 
# and write in any format