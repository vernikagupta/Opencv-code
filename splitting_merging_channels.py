# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 09:28:50 2020

@author: vernika
"""


'''OpenCV stores RGB images as NumPy arrays in reverse channel order. Instead of storing an image
in RGB order, it instead stores the image in BGR order; thus
we unpack the tuple in reverse order.'''


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

load_image = cv2.imread(args["image"])
b,g,r = cv2.split(load_image)
show_img(b)
show_img(g)
show_img(r)

merged = cv2.merge([b,g,r])
show_img(merged)

'''in order to check the original color of the channel, we first split the channels
as shown above then we use a zero mask of same dimension to show color. basically If we 
want to visualize red color, then we will use cv2.merge([0,0,r]) setting blue 
and green channel as zero'''

zeros = np.zeros(load_image.shape[:2], dtype = 'uint8')
merged = cv2.merge([zeros,zeros,r])
print("Visualizing red channel")
show_img(merged)