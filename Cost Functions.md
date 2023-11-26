# Cost Function/Error function
 An cost function measures how far our model deviates from correct prediction.

* it calculates the difference between the expected value and predicted value.
* Cost function plays a cruical role in understanding that how well your model estimate the relationship between the input and output parameters.
* different kind of cost function are used for different models to accurately determine the error.

##### Error = target - predicted

## 1. Regression cost function
Regression models are used to make a prediction for the continious variables such as the weather prediction, loan prediction etc.

#### a. Mean of means Error -
 In this type of cost function, the error is calculated for each training data, and then the mean of all error value is taken. The error that occured from the training data can be either negative or positive. while finding mean, they can cancel out each other and the result will the zero for model, so it is not useful function.

#### b. Mean squared Error(MSE) -
 It is most comonly used cost function. it improvees the drawbacks of the mean error function because as the name suggested we take sqaure of difference of actual and predicted value so we didn't get any negative value.

$$Error = \frac{1}{N}\sum (predicted - actual)^2$$

 It is also known as L2 loss

#### c. Mean absolute error(MAE) - 
 MAE also overcome the issue of the mean error cost function by taking absolute difference between the actual and predicted value.
 		
$$Error = |predcited - actual|$$

## 2. Binary Classification cost function

#### a. Binary crossentropy:
 This type cost function is used to make prediction when we have two classes only such classication is made by value 0(class 1) and 1(class 2).
 The commonly used cost function for classification is a cross-entropy loss. Binary classification is a special case of cross-entropy.
 cross-entropy loss is also known as log loss. entropy of a random variable x is the average level of the information.
 
 $$J(y, ŷ) = -frac{1}{N} \sum y_i * \log(\hat y_i)  + (1-y_i) * \log(1 - \hat y_i)$$
   
* ŷ: probability of class 1
* 1-ŷ: probability of class 0
   
#### b. Hinge loss(SVM loss):
it is often used in the context of support vector machine. it penalize misclassified points more severly then correctly classified points.

$$J(y, ŷ) = \frac{1}{N} \sum max( 0, 1 - y_i * ŷ_i)$$

## 3. Multi-class classification cost function

#### a. Softmax Loss(softmax cross entropy):
The softmax loss function is used in conjuction with softmax activation function in neural networks for multi-class classification.

$$softmax(\hat y_{ij}) =  \frac{ e^{\hat y_{ij}} } { \sum_{k=1}^{K} e^ŷ_{ik} }$$


$$J(y, ŷ) = -\frac{1}{N} \sum y_{ij} softmax(\hat y_{ij})$$
* yij: actual value of ith data-point from jth class(total k class)
* ŷij: predicted value of ith data-point from jth class

#### b. Sparse Multiclass Cross-entropy Loss:
This is a variation of cross entropy loss used when class labels are provided as integers(eg. class 0,1,2,...) rather than one-hot encoded vector

$$J(y, ŷ) = -\frac{1}{N} \sum yi * \log(ŷi)$$
        
#### c. Hinge Loss: 
It encourages the correct class score to be higher than the scores of other classes by a margin.

$$J(y, ŷ)  = \frac{1}{N} \sum \sum max(0, ŷ_{ij} - y_{ij} + Δ)$$

* Δ: margin parameter

#### d. Cross Entropy loss(Categorical Crossentropy):
Cross entropy is a widely used cost function for multi-class classification problems. It measures the dissimilarity between the predicted class and the true class labels.

$$J(y, ŷ) = -\frac{1}{N} \sum y_{ij} log(ŷ_{ij})$$


