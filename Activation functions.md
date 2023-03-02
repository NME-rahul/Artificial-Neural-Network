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

## 4. Leaky ReLU activation function

* The leaky ReLU activation function is a modifies version of the default ReLU function.
* Like the ReLU activation function, this function does have the vanishin gradient problem.
* IF the input is 0 or greater then 0, the leaky ReLU function outputs the input as it is like the default ReLU function deos. However, if the input is less then 0, the leaky ReLU function outputs a small negative value defined by 𝜶z(where 𝜶 is a small constant value, usually 0..1 and z is the input value).
* It don not have any linear component with zero derivatives(slopes) therefore, it can avoid dying ReLU problem.
* The learning process with leaky ReLU is faster then the defaut ReLU.

### Usage:
* The same usage of the ReLU function is also valid for the leaky ReLU function.

![Leaky ReLU activation function](https://miro.medium.com/v2/resize:fit:1200/format:webp/1*R15CMX7M8Fx_dlAuhZUlWA.png)


## 5. Parametric ReLU(PReLU) activation function
* This is another varient of the ReLU function.
* This is almost similar to the leaky ReLU function. the only difference is that the value 𝜶 becomes a learnable parameter(hence the name). We set 𝜶 as a prameter for each neuron in the network. Therfore, the optimal value of 𝜶 learns form the network.

## 6. ReLU6 activation function
* The main difference between ReLU and ReLU6 is that ReLU allows very high values on the positive side while ReLU6 restricts to the value 6 on the positive side.
* The ReLU6 function is made up of three linear components. it is a non-linear function.

![ReLU6 activation function](https://miro.medium.com/v2/resize:fit:1200/format:webp/1*P5EB-6rNeucah1F5_8a3KQ.png)


## 7. Binary step activation function
* This function is also known as the treshold activation function. we can set any value to the threshold and here we specify the value 0.
* If the input is greater than the threshold value, this function outputs the value 1. If the input is equal to the threshold value or less than it, this function outputs the value 0.
* This outputs a binary value, either 0 or 1.
* The binary step function is made up of the tow linear components. BEacuse of that, this function is a picewise linear function. In fact, the binary step function is anon-linear function.
* THis function is not a smooth function.

### Usage:
* In Practice, we don not usually ise this function in modern neural network models.
* owever, we can use this function to explain theortical concepts such as "firing a neuron", "inner working of a perceptron". Therfore, the step binary function is theoretically important.

![Binary step activation function](https://miro.medium.com/v2/resize:fit:1200/format:webp/1*kLXCnlfmGCRrLbZ_aSV6rg.png)

## 8. Identity activation function
* This also known as the linear activation function.
* This is the only function that is considered as a linear function when we talk about activation functions.
* This function outputs the input value as it is. No changes are made to the input.

### Usage:
* This function is only used in the output layer of a neural network model that saves a regression problem.

![Identity activation function](https://miro.medium.com/v2/resize:fit:1212/format:webp/1*h_-X4Ggt_YEWD58ha6x23w.png)
 
## 9. Tanh activation function
* The output of the tanh(tangent hyperbolic) always ranges between -1 and +1.
* Like the sigmoid function, it has an s-shaped graph. This is also a no-linear function.
* One advantage of using the tanh function over the sigmoid function is that the tanh function is zero centerd. This makes the optimization process much easier.
* The tanh function has a steeper gradient than the sigmoid function has.

### Usage:
* Until recently, the tanh function was used as an activation function for the hidden laer in MLPs CNNs and RNNs.
* However, the tanh function is stil use in RNNs.
* Currently, we do not usually use the tanh function for the hidden layers in MLPs and CNNs. instead, we use RELU or Leaky ReLU there.
* We never use the tanh function in the output layer.

### Drawbacks:
We don not usually use the tanh funcion in the hidden layer because of the following drawbacks.
* The tanh has the vaishing gradient problem.
* This funcion is computationaly expensive as e^z term is included.

![Tanh activation function](https://miro.medium.com/v2/resize:fit:1198/format:webp/1*qWEluqh-LVWC0Mt8vVNn_Q.png)

## 10. Swish activation function
* This function is made of by multiplying the sigmoid function by the input z.
* This is a non-linear function.
* The graph is much similar to the graph of the ReLU activation function.
* The curve is more smooth than the ReLU activation function. This ssmoothness is important when training the model. The functon converges while training.

### Usage:
* This function is only used in the hidden layers.
* We nevern use this function in the output layer of a neural network model.

### Drawbacks:
* The main drawbacks of the swish function is that is computationally expensive as e^z term is included in the function. This can be avoided by using special called "Hard Swish".

![Swish activation function](https://miro.medium.com/v2/resize:fit:1194/format:webp/1*9Fwkav2gO5kvx_OazeSx-g.png)

## 11. Hard Swish(H-Swish) activation function
* The graph is identical to the graph of the swish function.
* This is computationally inexpensive as the sigmoid was replace with a linear analogue.

### Usage:
* The usage of Hard-Swish is similar to the usage of the Swish activation function.

![Hard Swish(H-Swish) activation function](https://miro.medium.com/v2/resize:fit:1200/format:webp/1*vLyRo4eQ_evf2VslEwGttg.png)
