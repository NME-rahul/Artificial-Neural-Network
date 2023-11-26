# Convolution Operation

It is same convolution operation used in image processing. The convolutional operation is used to extract important features of the image, and throwing out unnecessary pixels(features). 

Convo operation reduces the image dimensions that saves the training time, reduces computation power and complexity of the model. It is denoted by the **"*"**

$$output = \frac{i - k + 2p}{s} + 1$$

* i: input image
* k: kernel filter size
* p: padding
* s: stride movement

---

<p align="center">
  <img src="https://pengfeinie.github.io/images/image-20211017144936783.png" height="" width="" />
</p>


Define kernel matrix and put kernel matrix on the image starting from left upper corner and move up unitl the you reach bottom right corner of the image, the movement steps is decided by the stride parameter.

Perform sum of products of the kernel's pixels with the coresponding pixels of the image that comes under the kernel dimension.

# Training CNN's

**Training parameters**
* kernel/filter
* Bias


<p align="center">
  <img src="https://private-user-images.githubusercontent.com/100432854/285640585-7061752c-5094-4b05-8b69-50bb25667fbe.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE3MDA5OTA1MjgsIm5iZiI6MTcwMDk5MDIyOCwicGF0aCI6Ii8xMDA0MzI4NTQvMjg1NjQwNTg1LTcwNjE3NTJjLTUwOTQtNGIwNS04YjY5LTUwYmIyNTY2N2ZiZS5qcGc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBSVdOSllBWDRDU1ZFSDUzQSUyRjIwMjMxMTI2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDIzMTEyNlQwOTE3MDhaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT01MDE1OTNhNDAxNTBlYjE3YTNiZDlkNjdlOGVkY2RjZWMzMjZiNjdmNjc3NDliYjlmMmJiOWU0YjRkMjdjMzMwJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.mu-JYIaG_XGuvOMTwaDdYVJw5g4tIQlmol5cow0tEjk" height="300" width="600"/>
</p>

## Forward pass

#### The Size of the output image after CNN layer
<p>
$$output Image = \frac{5 - 3 + 0}{1} + 1 = 3$$  
</p>

#### The Output image can be formulated as
  
  $$Y = I \circledast K + B$$
  
  $$\hat{Y} = activation(Y)$$

* **Y**: Output image matrix
* **I**: Input image matrix
* **K**: Kernel matrix
* **B**: Bias

#### The formula for calculating at a specific position i,j is given by

  $$y_{i,j} = \sum_{m=1}^{M} \sum_{n=1}^{N} (P_{i*s+m-1, j * s+n-1} * K_{i,j}) + b$$
  
  $$\hat y_{i,j} = activation(y_{i,j})$$

### Error calculation

Generally Binary Cross-Entropy, Categorical Cross-Entropy or Mean Squared Error is used, here we using Binary Cross-Entropy,

$$L(y, \hat{y}) = - y \log(\hat y) - (1-y)\log(1-\hat y)$$


## Backward pass

The updation of weights of kernel matrix are updated as we update the weights in conventional neural networks.

#### Chain Rule

$$\frac{\partial L(y, \hat y)}{\partial K} = \frac{\partial L(y, \hat y)}{\partial \hat y} * \frac{\partial \hat y}{\partial y} * \frac{\partial y}{\partial K}$$

$$\frac{\partial L(y, \hat y)}{\partial B} = \frac{\partial L(y, \hat y)}{\partial \hat y} * \frac{\partial \hat y}{\partial y} * \frac{\partial y}{\partial B}$$

#### Weight updation

$$K_{new} = K_{old} - \alpha * \frac{\partial L(y, \hat y)}{\partial K}$$

$$B_{new} = B_{old} - \alpha * \frac{\partial L(y, \hat y)}{\partial B}$$

* alpha: learning_rate

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
