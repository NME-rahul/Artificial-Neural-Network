## 1. Sigmoid function

* It is clearly a non-linear function.
* This is also called the logistic function used in logistic regression models.
* The sigmoid function has an s-shaped graph.
* The sigmoid function converts its input into a probability value between 0 and 1.
* It converts large negative values towards 0 and large positive values towards 1.
* It returns 0.5 for the input 0. The values 0.5 is know as the threshold value which can decide that given input belongs to what type of two classes.

### Usege:
* In the early days, the sigmoid function used as an activation function for the hidden layers in MLPs(Multi Layer Feedforward), CNNs and RNNs.
* However, the sigmoid function is still used in RNNs.
* Currently, we do not usually use the sigmoid function for the hidden layers in MLPs and CNNs. instead, we use ReLU or Leaky ReLU there.
* The sigmoid function must be used in the output layer when we build a binary classifier in which output is interpreted as class label depending on the probability value of input returned by the function.

### Drawbacks:
We do not sually use the sigmoid function in the hidden layer beacause of the following drawbacks.
* The sigmoid fucntion has the vanishing gradient problem. This is also knwon as saturaton of the gradients.
* THe sigmid function has slow convergence.
* its outputs are not zero-centerd. therfore, it makes the optimization process harder.
* This function is computationally expensive as an e^x term is included.

![sigmoid function](https://miro.medium.com/v2/resize:fit:1200/format:webp/1*SuwKNT1Y9K9dsD5Dzm5I_g.png)


## 2. ReLU Activation function

* The ReLU(Rectified Linear unit) activation function is a great alternative to both sigmoid and tanh activation function.
* This function doesn't have the vanishing gradient problem.
* This function is computtationally inexpensive. It is considered that the convergence of ReLU is 6 time faster then sigmoid and tanh function.
* If the input value is 0 or greater then 0, the ReLU function output s the input as it is. If the input is less then 0, the ReLU function outputs the value 0.
* The ReLU function is made up of two linear components, Beacuse of that, the ReLU function is a picewise(out put 0 for less then 0 otherwise same as input) linear function. In fact, the ReLU function is a non-linear function.
* The output of the ReLU function can range from 0 to positive infinity.
* The convergence is faster than sigmoid and tanh functions. this is because the ReLU function has fixed derivate(slope) for one linear component and a zero derivate for other linear component. Therefore, the learning process is much faster with the ReLU function.
* Calculations can be performed much faster with ReLU because no exponential term are included in the function.

### Usage:
* The ReLU function is the default activation function for hidden layers inmodern MLP and CNN neural network model.
* We do not use the ReLU function in the hidden layers of RNN model. Instead, we use the sigmoid or tanh function there.
* We never use the ReLU function in the output layer.

### Drawbacks:
* The main drawbacks of using the ReLU function is that it has a dying ReLU problem.
* The Value of the positive side can go very high. that may lead to a computational issue during the training.

![ReLU Activation function](https://miro.medium.com/v2/resize:fit:1200/format:webp/1*rsyrrFMTwULMw32bjW7JgQ.png)


## 3. Softmax activation function

<img src="https://miro.medium.com/v2/resize:fit:816/format:webp/1*WWTFPwIgU_iV_Q1l_Co-Uw.png" style="left-margin:20%;">

* This is also a non-linear activation function.
* The softmax function calculates the probability value of an event(class) over k different events(classes). IT calculates the probability values for each class. The sum of all probabilities is 1 meaning that all events are mutually exclusive.

### Usage:
* We must use the softmax function in the output layer of a multiclass classification problem.
* we never use the softmax function in the hidden layers.
