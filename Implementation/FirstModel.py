''' 
we are implemeting the simplest function y = wx
where y: output
      w: weight
      x: input

-> the function has only one trainable parameter w.

      input       output      prediction      Error
1       2           4             3             1
2       4           6             5             1
3       7           9             8             1
                                           ----------
                                            sum = 3
                                            
-> here the error is 3 but it Error has to be 0 or near 0 to do this we have to adjust the weight.

-> simplest way to get weight is w = y/x

      weight
1       2.00
2       1.50
3       1.28

-> weight is different for different sample inputs to overcome this problem a new variable is itroduced id called bias.

-> Now the function is y = wx + b, it is a mathmatical repersentation of neuron in ANN.
-> function for multiple inputs is y = W1X1 + W2X2 + .... + WnXn + b
-> we will adjust the value of weights corresponding to the inputs in training phase.
-> b(bias) is a constant value for a neuron.

->
'''

import numpy

