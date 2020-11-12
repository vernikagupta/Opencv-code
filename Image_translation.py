# -*- coding: utf-8 -*-

from __future__ import print_function
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
print(args)

load_image = cv2.imread(args["image"])
show_img(load_image)

'''Translation means shifting image along X and Y axis. We can shift the image
left, right, Up, down'''

M = np.float32([[1,0,25], [0,1,50]])
'''Translation matrix shifed downa and right'''
shifted = cv2.warpAffine(load_image, M, (load_image.shape[1],load_image.shape[0]))
show_img(shifted)


M = np.float32([[1,0,-50], [0,1,-90]])
'''Translation matrix shifed Up and left'''
shifted = cv2.warpAffine(load_image, M, (load_image.shape[1],load_image.shape[0]))
show_img(shifted)

'''M should be float only
[1,0,tx] where tx is no of pixels we want to shhift the image left or right
positive tx means shifting right and negative tx means left shift

[0,1,tx] positive tx means shift down and -ve tx means Up'''