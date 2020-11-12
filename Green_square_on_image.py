#Program to crop 100* 100 section of image and modify the image
# Draw a green square on 100* 100 section of image

from __future__ import print_function
import cv2
import argparse


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "path to image")
args = vars(ap.parse_args())

load_image = cv2.imread(args["image"])
cv2.imshow("original", load_image)
cv2.waitKey(0)
# crop the first 100*100 swction of image
#load_image[ystart : yend, xstart: xend]
corner = load_image[0:100, 0:100]
cv2.imshow("corner", corner)
cv2.waitKey(0)


# Manupilate the upper 100*100 section of image
load_image[0:100, 0:100] = (0,128,0)
cv2.imshow("updated", load_image)
cv2.waitKey(0)
