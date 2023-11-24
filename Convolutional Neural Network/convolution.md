# Convolution Operation

It is same convolution operation used in image processing. The convolutional operation is used to extract important features of the image, and throwing out unnecessary pixels(features). 

Convo operation reduces the image dimensions that saves the training time, reduces computation power and complexity of the model.


<p align="center">
  <img src="https://pengfeinie.github.io/images/image-20211017144936783.png" height="" width="" />
</p>


Define kernel matrix and put kernel matrix on the image starting from left upper corner and move up unitl the you reach bottom right corner of the image, the movement steps is decided by the stride parameter.

Perform sum of products of the kernel's pixels with the coresponding pixels of the image that comes under the kernel dimension.
