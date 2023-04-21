import numpy as np
imo
import activationFunctions as af

def squaredError(prediction, target):
    return np.power((prediction - target), 2)

def error_prediction_deriv(prediction, target):
    return 2 *(predicted - target)

def sop_w_deriv(x):
    return x
    
def forwardPropgation(model, data, epochs, num_class, target):
    prediction = []; result = np.array([]); 
    num_inputs = model[0]['info']['num_inputs']
    num_neurons = model[1]['info']['num_neurons']
    sops = []; temp = 0
    for p in range(epochs):
        #for input layer
        for i in range(num_inputs):
            for j in range(num_neurons):
                temp = temp + (data[i][0] * model[0]['weight'][j][i])
            temp = af.activation(temp, activationFun =  model[0]['info']['activationFun'])
            sops.append( temp )
            
        #for hidden layers
        for k in range(1, len(model) - 1):
            for i in range(num_neurons):
                for j in range(num_neurons):
                    temp = sops[i] * model[k]['weight'][j][i]
                temp = af.activation(temp, activationFun = model[1]['info']['activationFun'])
                sops.append( temp )
            
        #for output layer
        for i in range(num_class):
            for j in range(num_neurons):
                temp = temp + (sops[j*-1 - 1] * model[-1]['weight'][j*-1 - 1][i*-1 - 1])
            sops.append( temp ) #it appends the last nrurons output first
        
        for i in range(num_class):
            prediction.append(af.activation(sops[i*-1 - 1], activationFun =  model[-1]['info']['activationFun'])) #now we again reverse the order(of output layer) of vlaues so it come again in its original order.
            result = np.append(result, prediction[i])
            result = np.append(result, squaredError(prediction[i], target[i]))
            
    result.reshape(epochs, 2)
            
    print(result)
                
    return result
    
def update_w(weight, learning_rate, grad):
    return weight + (learning_rate * grad)
    
def backwardPropogation(model, epochs, num_class, learning_rate):
    return
