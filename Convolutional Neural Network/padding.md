# Padding

If you want to preserve all the pixels of image then padding is used on the image so filter can go through over the all pixels of the image and produces output image as the same size of input of image.

$$output = [\frac{i - k + 2p}{s}] + 1$$

<p align="center">
  <img src="https://github.com/NME-rahul/Artificial-Neural-Network/assets/100432854/0fa0398c-7f44-41dc-b788-6bbbe204c9f3" height="" width=""/>
</p>

**Why padding?**
* It removes the boarder problem.
* Some of the pixel in image won't get the same chance of participation in filter convolution as other, to overcome this problem padding is used.

**How to do padding?**
Padding is done by adding zeros to the boundary of the input image.

  $$ padding = \lfloor K / 2 \rfloor$$
