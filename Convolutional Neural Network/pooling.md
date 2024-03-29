# Pooling

Pooling is required to down sample the detection of features in feature maps. Pooling layer provide an approach to down sampling the features by summarizing the presence of features in patches on the feature map.

  $$output = \lfloor \frac{i}{k} \rfloor$$

Th goal of the pooling is to reduce the dimensionality of the image while keeping mportant features of the image. Pooling is done in patches meaning one pixel will not take participate more then on time.

  <p align="center">
     <img src="https://miro.medium.com/v2/resize:fit:1400/1*fXxDBsJ96FKEtMOa9vNgjA.gif"  height="250px" width="500px"/>
   </p>

#### Pooling methods

1. **Average pooiling:** It summarize the features of image by taking average of pixels that lies in the filter.

    <p align="center">
     <img src="https://androidkt.com/wp-content/uploads/2021/06/max-pooling.png"  height="250px" width="500px"/>
   </p>
  
3. **Max pooling**: It summarize the features of image by choosing maximum pixel value that lies in the filter.

   <p align="center">
     <img src="https://miro.medium.com/v2/resize:fit:1400/1*WvHC5bKyrHa7Wm3ca-pXtg.gif"  height="250px" width="400px"/>
   </p>

---

Tensorflow syntax:

    model = tf.keras.model.Sequential([
            tf.keras.layers.MaxPooling2D(pool_size, stride, padding, data_formatinput_shape)
    ])

Max pooling

    pool_layer = tf.keras.layers.MaxPooling2D(pool_size, stride, padding, data_format)(input_shape)

Average pooing

    pool_layer = tf.keras.layers.AveragePooling2D(pool_size, stride, padding, data_format)(input_shape)


* **pool_size**: represents the pooling filter dimension, eg. (2,2).
* **stride**: specify the movement per steps of the pooling filter, eg. (1, 2) in (height, width) format, by default (1, 1).
* **padding**: "valid" for no padding or "same" for zero padding.
* **data_format**: specify the output format of the layer, eg. (batch, height, width, channels) or batch, channels, height, width)
* **input_shape**: specify the input matrix on the layer.
