# Stride

The amount of movement in between input image by the filter is refered as the stride. It is almost symmetrical in height and width dimensions.

The default stride or stride in two dimensions is (1,1) for height and width movement.

$$Output = [\frac{i - k}{s}] + 1$$

* i: input image size
* K: kernel size
* S: pixel movement by the filter each time

<p align="center">
  <img src="https://pengfeinie.github.io/images/image-20211017144936783.png" height="" width="500" />
</p>

<p align="center">
  <img src="https://pengfeinie.github.io/images/image-20211017145212919.png" height="" width="500" />
</p>
