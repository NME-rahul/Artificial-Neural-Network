import numpy as np

def error_prediction_deriv(predicted, target):
    return 2 * (predicted - target)
    
def prediction_sop_deriv(sop):
    return sigmoid(sop) * (1 - sigmoid(sop))
    
def sop_w_deriv(x):
    return x

def sop_activ_deriv(active):
    return sigmoid(active) * (1 - sigmoid(active))
    
def update_w(w, learning_rate, grad):
    return w - (learning_rate * grad)
    
def CalculateSOP(inputs, weights, col):
    sop = 0
    for row in range(len(inputs)):
        sop = sop + inputs[row] * weights[row][col]
    return sop
    
def sigmoid(sop):
    return 1.0 / (1 + np.exp(-1 * sop))
    
def squaredError(predicted, target):
    return np.power((predicted - target), 2)
    
def main():
    target = 0.2; error = 0.0; learning_rate = 0.001
    inputs = np.array([np.random.random(), np.random.random(), np.random.random()])
    
    weights1 = np.array([i for i in np.random.rand(6)]).reshape(3, 2)
    weights2 = np.array(np.random.rand(2)).reshape(2, 1)
    
    for k in range(int(input('Epochs: '))):
        #forward pass
        sop = [CalculateSOP(inputs, weights1, 0), CalculateSOP(inputs, weights1, 1)]
        active = np.array([sigmoid(sop[0]), sigmoid(sop[1])])
    
        sop21 = CalculateSOP(active, weights2, 0)
        predicted = sigmoid(sop21)
    
        error = squaredError(predicted, target)
        
        print('\nIteration %d:- \nError: %2.6f  Predicted: %2.6f  target: %2.6f'%(k, error, predicted, target))
        #backward pass
        #output layer
        for i in range(2):
            grad =  error_prediction_deriv(predicted, target) * prediction_sop_deriv(sop21) * sop_w_deriv(active[i])
            weights2[i][0] = update_w(weights2[i][0], learning_rate, grad)
        
        #hidden layer
        for i in range(2):
            for j in range(3):
                grad = error_prediction_deriv(predicted, target) * prediction_sop_deriv(sop21) * sop_w_deriv(weights2[i][0]) * prediction_sop_deriv(sop[i]) * sop_w_deriv(weights1[j][i])
                weights1[j][i] = update_w(weights1[j][i], learning_rate, grad)
            
    print('\n\nWeights:- \nInput-Hidden Layer: \n', weights1, '\n\nHidden_Output Layer: \n', weights2)
        
                
main()
