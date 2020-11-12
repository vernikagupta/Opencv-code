# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 11:15:40 2020

@author: vernika
"""

'''Histogram plotting gives us high level intutuion about contrast, brightness
and intensity distribution. command to plot histogram is
cv2.calcHist(images,channels,mask,histSize,ranges)'''

import cv2
import argparse
import matplotlib.pyplot as plt


def show_img(img):
    cv2.imshow("canvas",img)
    cv2.waitKey(0)
    return

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "path to image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

# Grayscale Histogram
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
hist = cv2.calcHist([image], [0], None, [256], [0, 256])
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()
cv2.waitKey(0)


# colour histogram
image = cv2.imread(args["image"])
chans = cv2.split(image)
colors = ("b", "g", "r")
plt.figure()
plt.title("’Flattened’ Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
for (chan, color) in zip(chans, colors):
    hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
    plt.plot(hist, color = color)
    plt.show()
    cv2.waitKey(0)
 
'''Pairwise 2D plotting of Histogram'''
fig = plt.figure()

ax = fig.add_subplot(131)
hist = cv2.calcHist([chans[1], chans[0]], [0, 1], None,
[32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation = "nearest")
ax.set_title("2D Color Histogram for G and B")
plt.colorbar(p)
plt.show()
cv2.waitKey(0)


ax = fig.add_subplot(132)
hist = cv2.calcHist([chans[1], chans[2]], [0, 1], None,
[32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation = "nearest")
ax.set_title("2D Color Histogram for G and R")
plt.colorbar(p)
plt.show()
cv2.waitKey(0)

ax = fig.add_subplot(133)
hist = cv2.calcHist([chans[0], chans[2]], [0, 1], None,
[32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation = "nearest")
ax.set_title("2D Color Histogram for B and R")
plt.colorbar(p)
plt.show()
cv2.waitKey(0)

print("2D histogram shape: {}, with {} values".format(hist.shape, hist.flatten().shape[0]))


'''Note when we are working with 2D histograms, then we keep bins between 8 to 64.
256 bins of each channel means 256*256 bins which is not a practical thing'''
