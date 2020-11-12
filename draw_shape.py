import numpy as np
import cv2


def show_img(img):
    cv2.imshow("canvas",img)
    cv2.waitKey(0)
    return


canvas = np.zeros((300,300,3), dtype= 'uint8')

green = (0,255,0)
cv2.line(canvas, (0,0), (300,300), green)  # (0,0) starting coordinate and
                                            # (300,300) ending coordinate
show_img(canvas)

red = (0,0,255)
cv2.line(canvas, (0,300), (300,0), red, thickness=5)
show_img(canvas)


cv2.rectangle(canvas, (10,10), (60,60), green)
show_img(canvas)

cv2.rectangle(canvas, (50,200), (200,225), green, thickness=3)
show_img(canvas)


cv2.rectangle(canvas, (200,200), (250,225), red, thickness=-1)
show_img(canvas)

#-1 to fill the rectanagle


### Draw circle
''' To draw circle on image, we first find the center (x,y) coordinate of image'''

canvas = np.zeros((300,300,3), dtype='uint8')
centerx, centery = (canvas.shape[1]//2, canvas.shape[0]//2)
white = (255,255,255)

for r in range(0,175,25):
    cv2.circle(canvas, (centerx, centery), r, white)
    
show_img(canvas)


# we loop over a number of radius and increament by 25
# the dot in the very center is drawn by radius of zero






