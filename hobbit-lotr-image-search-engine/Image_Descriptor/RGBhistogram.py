# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 12:11:43 2021

@author: vernika
"""

import cv2

# feature descriptor (3D color histogram)

class RBGHistogram:
  def __init__(self, bins):
    # store the no of bins histogram will use
    self.bins = bins   # assume self.bins is a list of three integers, designating the number of bins for each channel.

  def describe(self, image):
    # compute 3D color histogram of given image
    # and normalize the histogram so that images
    # having same content but different scale and will
    # have roughly same histogram

    hist = cv2.calcHist([image], [0,1,2], None, self.bins, [0,256, 0, 256, 0, 256])

    # normalize with OpenCV
    hist = cv2.normalize(hist, hist)

    # return 3D histogram in a flattened array
    return hist.flatten()


