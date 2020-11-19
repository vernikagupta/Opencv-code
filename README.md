#### Opencv-code

Basic opencv code for performing operations on images such as cropping, masking, blurring, Histogram techniques, Thresholding, Edge detection and contouring.
#### To run any code file
* Python filename.py -i path to input image

###### Some Important points to Note

* <b>Coordinate system for Image:</b> The origin (0, 0) of an image starts at the top-left corner of the image and increases as we move to the right and down. We specify pixels in terms of (x,y) coordinate but Image is basically defined as a matrix means <b>x represent number of columns and <b> y represents number of rows</b>. So, to specify a pixel, we first enter y and then x. 
  <br> Image[y,x]</br>
* OpenCV stores image in <b>BGR format rather than RGB format</b>

* <b>Color Space:</b> There are mainly used 3 color space BGR, HSV, L*A*B. RGB is easy to understand but not intutive if we want to pick a particular shade of color or we want to specify particular color. In that case, <b>HSV is useful for defining exact shades of a color if you need to define a particular range of colors (useful when tracking objects in a video stream based on color appearance).</b>
The HSV color space tends to be more intuitive in terms of actually defining a particular color (or range), but it doesn’t do a great job of representing how humans see and interpret color.
<b>Then we have the L*a*b* color space — this color space tries to mimic the methodology in which humans see and interpret color. This implies that the Euclidean distance between two arbitrary colors in the L*a*b* color space have actual perceptual meaning.</b>

The addition of the perceptual meaning property makes the L*a*b* color space less intuitive and easy to understand than RGB or HSV, but because of the perceptual meaning property, we often use it in computer vision.

** Positive values of angle will rotate an image counter-clockwise and negative values clockwise.
