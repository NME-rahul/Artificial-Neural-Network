''' 
-> this neuron has only one input and one output and no hidden layer.
-> the neuron is capable only to forward the signal.

SOP = XW

-> sigmoid function is use as a activation function.
      sigmoid = 1 / 1 + e^(-SOP)
      
-> We are assuming the output will lie between 0 to 1. if there is two classes(c1 and c2) then class c1 if output is less then equal to 0.5 otherwise class c2.

-> After calculating the predicted output we will measure the prediction error.
      error = $\sum_{n=0}to{n=N} (predicted - real)^2
      
 -> after calculation of prediction error, the forward pass is complete.
 
 Forward Pass:
-> let initialy W = 0.5 and X = 2, y = 1 then SOP = 1.0 and 
-> sigmoid = 1 / 1 + e^(-1.0) => 0.73105857863
-> output is 0.7
-> error = (0.7 - 1.0)^2 = 0.09

 
 Backaward pass:
 -> in backward pass we will try to adjust the value of weight to minimize the error.
 -> To minimize the error we will do differentitaion of error w.r.t to W{d(error)/dW} and set it to equal to zero.
 -> weight gradient => dError/dW = dError/dPredicted * dPredicted/dSOP * dSOP/dW
          dError/dPredected = 2(predicted - real) = 2(0.7 - 1.0) = -0.6
          dPredected/dSOP = (1 / 1 + e^-SOP) * (1 - (1 / 1 + e^-SOP)) = (0.534) * (0.36) = 0.196
          dSOP/dW = X = 2
          dError/dW = -0.6 * 0.196 * 2 = -0.2352
 
-> weight adjustment formula is W(new) = W(old) - learning_rate * grad
      W(new) = 0.5 - 0.01 * (-0.2352) = 0.502352
      
-> the new weight is grater then older one, we will repeat this step and adjust the value of weight until we find the apropriate weight.
 '''


''' 
-> this neuron has only one input and one output and no hidden layer.
-> the neuron is capable only to forward the signal.

SOP = XW

-> sigmoid function is use as a activation function.
      sigmoid = 1 / 1 + e^(-SOP)
      
-> We are assuming the output will lie between 0 to 1. if there is two classes(c1 and c2) then class c1 if output is less then equal to 0.5 otherwise class c2.

-> After calculating the predicted output we will measure the prediction error.
      error = $\sum_{n=0}to{n=N} (predicted - real)^2
      
 -> after calculation of prediction error, the forward pass is complete.
 
 Forward Pass:
-> let initialy W = 0.5 and X = 2, y = 1 then SOP = 1.0 and 
-> sigmoid = 1 / 1 + e^(-1.0) => 0.73105857863
-> output is 0.7
-> error = (0.7 - 1.0)^2 = 0.09

 
 Backaward pass:
 -> in backward pass we will try to adjust the value of weight to minimize the error.
 -> To minimize the error we will do differentitaion of error w.r.t to W{d(error)/dW} and set it to equal to zero.
 -> weight gradient => dError/dW = dError/dPredicted * dPredicted/dSOP * dSOP/dW
          dError/dPredected = 2(predicted - real) = 2(0.7 - 1.0) = -0.6
          dPredected/dSOP = (1 / 1 + e^-SOP) * (1 - (1 / 1 + e^-SOP)) = (0.534) * (0.36) = 0.196
          dSOP/dW = X = 2
          dError/dW = -0.6 * 0.196 * 2 = -0.2352
 
-> weight adjustment formula is W(new) = W(old) - learning_rate * grad
      W(new) = 0.5 - 0.01 * (-0.2352) = 0.502352
      
-> the new weight is grater then older one, we will repeat this step and adjust the value of weight until we find the apropriate weight.
 '''


import numpy as np

def sigmoid(sop):
      return 1.0 / (1 + np.exp(-1 * sop))

def error(predicted, real):
      return np.power(predicted - real, 2)

def error_prediction_deriv(predicted, real):
      return 2 * (predicted - real)

def prediction_sop_derv(sop):
      return sigmoid(sop) * (1.0 - sigmoid(sop))

def sop_w_deriv(x):
      return x;

def update_w(w, grad, learning_rate):
      return w - (learning_rate * grad)

x = 2
real = 1.0
learning_rate = 0.01
w = np.random.rand()

print("initial w: ", w)

for i in range(int(input('Enter epoches: '))):
      # Forward pass
      y = w * x
      predicted = sigmoid(y)
      err = error(predicted, real)
      print("Prediction: %f, Error: %f, weight: %f" %(predicted, err, w))
      
      #Backward pass
      g1 = error_prediction_deriv(predicted, real)
      g2 = prediction_sop_derv(y)
      g3 = sop_w_deriv(x)

      grad = g1 * g2 *g3
      

      w  = update_w(w, grad, learning_rate)
