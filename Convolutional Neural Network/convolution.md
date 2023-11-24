# Convolution Operation

It is same convolution operation used in image processing. The convolutional operation is used to extract important features of the image, and throwing out unnecessary pixels(features). 

Convo operation reduces the image dimensions that saves the training time, reduces computation power and complexity of the model. It is denoted by the **"*"**


<p align="center">
  <img src="https://pengfeinie.github.io/images/image-20211017144936783.png" height="" width="" />
</p>


Define kernel matrix and put kernel matrix on the image starting from left upper corner and move up unitl the you reach bottom right corner of the image, the movement steps is decided by the stride parameter.

Perform sum of products of the kernel's pixels with the coresponding pixels of the image that comes under the kernel dimension.

---

Tensorflow syntax

    model = tf.keras.model.Sequential([
            tf.keras.layers.Conv2D(filters, kernel, padding, use_bias, strides, activation, input_shape)
    ])


another type

    conv_layer = tf.keras.layers.Conv2D(filters, kernel, padding, use_bias, strides, activation)(input_shape)


* **filters**: reprsent the number of different type of filters you want to use, and layer will produce diffrent output matrix for each filter.
* **padding**: "valid"(case-sensitive) for no padding, "same" for zero padding, adds the boarder to the image so the dimesnion of the input and output image will remain same.
* **use_bias**: take boolean value True or False.
* **stride**: specify the movement steps at once.
* **activation**: specify activation function.
* **input_shape**: specify input image shape, for first layer only if input layer is not used.
