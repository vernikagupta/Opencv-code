# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 09:43:06 2020

@author: vernika
"""

import cv2
import argparse


def show_img(img):
    cv2.imshow("canvas",img)
    cv2.waitKey(0)
    return

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "path to image")
args = vars(ap.parse_args())

load_image = cv2.imread(args["image"])
show_img(load_image)

gray = cv2.cvtColor(load_image, cv2.COLOR_BGR2GRAY)
show_img(gray)

hsv = cv2.cvtColor(load_image, cv2.COLOR_BGR2HSV)
show_img(hsv)

lab = cv2.cvtColor(load_image, cv2.COLOR_BGR2LAB)
show_img(lab)