# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 17:04:39 2020

@author: vernika
"""

'''When we want to perform histogram plotting or equalization only on the 
masked area of image'''


import cv2
import argparse
import numpy as np
import matplotlib.pyplot as plt


def plot_histogram(image, title, mask = None):
    chans = cv2.split(image)
    colors = ("b", "g", "r")
    plt.figure()
    plt.title(title)
    plt.xlabel("Bins")
    plt.ylabel("# of Pixels")
    for (chan, color) in zip(chans, colors):
        hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
        plt.plot(hist, color = color)
        plt.xlim([0, 256])
        plt.show()
        
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "path to image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)
plot_histogram(image, "Histogram for Original Image")


mask = np.zeros(image.shape[:2], dtype = "uint8")
cv2.rectangle(mask, (15, 15), (130, 100), 255, -1)
cv2.imshow("Mask", mask)
cv2.waitKey(0)
masked = cv2.bitwise_and(image, image, mask = mask)
cv2.imshow("Applying the Mask", masked)
cv2.waitKey(0)

plot_histogram(image, "Histogram for Masked Image", mask = mask)
plt.show()