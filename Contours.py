# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 21:44:52 2020

@author: vernika
"""

'''Contours are used to find curves in an image. Contour is a curve of points 
with no gap in curve. used for shape approximation and analysis. In order to find contours in an image, you need to first obtain a binarization of the image, using either edge detection
methods or thresholding'''

import cv2
import argparse

def show_img(w_name,img):
    cv2.imshow(w_name, img)
    cv2.waitKey(0)
    return

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "path to image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (11, 11), 0)
edged = cv2.Canny(blurred, 30, 150)
(_, cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
print("I count {} counters in this image".format(len(cnts)))
coins = image.copy()
cv2.drawContours(coins, cnts, -1, (0, 255, 0), 2) # -1 to show all countours
show_img("contours", coins)

# (0,255,0) represent green color
# 2 represent thickness of drawn contour

#Let’s crop each individual object from the image:
for (i, c) in enumerate(cnts):
    (x, y, w, h) = cv2.boundingRect(c)
    print("object #{}".format(i + 1))
    coin = image[y:y + h, x:x + w]
    show_img("object",coin)

