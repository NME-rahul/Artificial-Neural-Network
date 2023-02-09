## Introduction to Perceptron
* It is a first model of ANN with supervised learning.
* It is used for clasification of patterns that are linearly seprable.
* It consist of single neuron(input and output layer only) with adjustable synaptic weight and bias.

<img src="https://www.simplilearn.com/ice9/free_resources_article_thumb/Perceptron/general-diagram-of-perceptron-for-supervised-learning_4.jpg" alt="Perceptron" style="left-margin:50px;">

---

* as we know perceptron is built on single neuron so it is limited to perform classification with only two classes.
* By expanding the output layer to include more than one neurons, classification with more than two classes can be done(classes have to be linearly seprable).

<img src="https://upload.wikimedia.org/wikipedia/commons/a/af/Linearly_separable_red-blue_cropped_.svg" alt="linearly-seprable-data" class="inearly-seprable-data" margin="10%">
<label for="inearly-seprable-data">Linearly seprable Data</label>

<br><br>

**General Formula: $\sum_{n=1}^{n=m} _WiXi_ + _b_**

* adding bias makes the classification correct, without bias the hyperplane will always go through the origin.
* Every neural netwrok including percetron classify the data according to activation function.

    | +1 if  y > 0
    | 0  if  y = 0
    | -1 if  y < 0

