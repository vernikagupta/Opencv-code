# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 13:56:50 2020

@author: vernika
"""

'''Perform bitwise operations AND, OR, NOT, XOR  on images.
Bitwise operators operate in binary mode and represented as grayscale image
If a pixel value is greater than 0 then turned ON, otherwise turned OFF'''


import numpy as np
import cv2

def show_img(img):
    cv2.imshow("canvas",img)
    cv2.waitKey(0)
    return

rectangle = np.zeros((300,300), dtype = 'uint8')
cv2.rectangle(rectangle, (25,25), (275,275), 255, -1)
show_img(rectangle)

circle = np.zeros((300,300), dtype = 'uint8')
cv2.circle(circle, (150,150), 150, 255, -1)
show_img(circle)

bitwiseAnd = cv2.bitwise_and(rectangle, circle)
show_img(bitwiseAnd)


bitwiseOr = cv2.bitwise_or(rectangle, circle)
show_img(bitwiseOr)

bitwiseXor = cv2.bitwise_xor(rectangle, circle)
show_img(bitwiseXor)

bitwiseNot = cv2.bitwise_not(circle)
show_img(bitwiseNot)
