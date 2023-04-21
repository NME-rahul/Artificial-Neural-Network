import numpy as np

def activation(sop, activationFun):
    if activationFun == 'sigmoid':
        return 1 / (1 + np.exp(-1 * sop))
    
    if  activationFun == 'softmax':
        return 
    
    if activationFun == 'relu':
        return
    
    if activationFun == 'relu6':
        return
    
    if activationFun == 'leaky_relu':
        return
    
    if activationFun == 'perm_relu':
        return
    
    if activationFun == 'binary_step':
        return
    
    if activationFun == 'iden':
        return
    
    if activationFun == 'swish':
        return
    
    if activationFun == 'hard_swish':
        return
    
    if activationFun == 'tanh':
        return


def sop_activation_deriv(sop, activationFun):
    if activationFun == 'sigmoid':
        return activation(sop, activationFun) * (1 - activation(sop, activationFun))
    
    if  activationFun == 'softmax':
        return 
    
    if activationFun == 'relu':
        return
    
    if activationFun == 'relu6':
        return
    
    if activationFun == 'leaky_relu':
        return
    
    if activationFun == 'perm_relu':
        return
    
    if activationFun == 'binary_step':
        return
    
    if activationFun == 'iden':
        return
    
    if activationFun == 'swish':
        return
    
    if activationFun == 'hard_swish':
        return
    
    if activationFun == 'tanh':
        return
