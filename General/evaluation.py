import numpy as np
import activationFunctions

def sopOut(sop, activationFun):
    return 

def squaredError(prediction, target):
    return np.power((prediction - target), 2)
    
def forwardPropogation(model, data, epochs, num_class, target):
    result = np.array([])
    num_neurons = model[1]['info']['num_neurons']
    sops = []; temp = 0
    for i in range(epochs):
        
        #for input layer
        for i in range(num_neurons):
            for j in range(num_neurons):
                temp = temp + (data[i][0] * model[0]['weight'][j][i])
            temp = activation(sop, activationFun =  model[0]['info']['activationFun'])
            sops.append( temp )
            
        #for hidden layers
        for k in range(len(model - 2)):
            for i in range(num_neurons):
                for j in range(num_neurons):
                    temp = sops[i] * model[k + 1]['weight'][j][i]
                temp = activation(sop, activationFun = model[1]['info']['activationFun'])
                sops.append( temp )
            
        #for output layer
        for i in range(num_class):
            for j in range(num_neurons):
                temp = temp + (sops[j*-1 - 1] * model[-1]['weight'][j*-1 - 1][i*-1 -1])
            sops.append( temp ) #it appends the last nrurons output first
        
        for i in range(num_class):
            prediction = activation(sop[i*-1 -1], activationFun =  model[-1]['info']['activationFun']) #now we again reverse the order(of output layer) of vlaues so it come again in its original order.
            np.append(result, prediction, squaredError(prediction[i], target[i]))
            
        result.reshape(num_class, 2)
                
    return result
    
def update_w(weight, learning_rate, grad):
    return weight + (learning_rate * grad)
    
def backwardPropogation(model, epochs, num_class, learning_rate):
    return 
    
    