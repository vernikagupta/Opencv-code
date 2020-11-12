'''Rotation of an image means rotating through an angle and we normally rotate the 
image by keeping the center. so, first we will calculate center of an image
and then we will rotate through given angle. We can rotate by taking any point on
image, more preferably center'''

from __future__ import print_function
import cv2
import argparse

def show_img(img):
    cv2.imshow("canvas",img)
    cv2.waitKey(0)
    return


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "path to image")
args = vars(ap.parse_args())
print(args)

load_image = cv2.imread(args["image"])
#show_img(load_image)

h,w  = load_image.shape[:2]
print(h,w)

Center = (h//2,w//2)
print(Center)

M = cv2.getRotationMatrix2D(Center, 45, 1.0)
rotated = cv2.warpAffine(load_image, M, (w,h))
show_img(rotated)


'''45 degree is the angle we are rotating the image and 1.0 is the scale
1.0 means same size of original. 2.0 means double the size, 0.5 means half the soze
of image'''