# Padding

If you want to preserve all the pixels of image then padding is used on the image so filter can go through over the all pixels of the image and produces output image as the same size of input of image.

$$output = [\frac{i - k + 2p}{s}] + 1$$


**Why padding?**
* It removes the boarder problem.
* Some of the pixel in image won't get the same chance of participation in filter convolution as other, to overcome this problem padding is used.

**How to do padding?**
Padding is done by adding zeros to the boundary of the input image.

  $$ padding = \lfloor K / 2 \rfloor$$
