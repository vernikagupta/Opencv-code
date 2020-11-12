"""
Created on Tue Nov  3 12:53:57 2020

@author: vernika
"""

from __future__ import print_function
import cv2
import argparse



''' to resize image we have to take account of aspect ration.
If we know the width f new image, then we will divide the new width to old width 
and get a ratio. Then we will multiply the old height to ratio to get the new height.

if we know the new height of image, then same procedure for width'''


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

old_h,old_w  = load_image.shape[:2]
new_w = 150

r = new_w/old_w
dim = (150, int(old_h * r))
resized = cv2.resize(load_image, dim, interpolation = cv2.INTER_AREA)
show_img(resized)

'''interpolation is the algorithm that works behind the scene and 
cv2.InterARea works best among all'''