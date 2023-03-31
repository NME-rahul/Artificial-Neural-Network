import numpy as np

def Input(num_inputs, activationFun, name = 'Input_layer', **features):
    weight = np.array([i for i in np.random.rand(num_inputs * num_inputs)]).reshape(num_inputs, num_inputs)
    return {'weight': weight, 'info': {'num_inputs': num_inputs, 'activationFun': activationFun, 'name': name}}
        
        
def Hidden(num_neurons, activationFun, edges = 'fully_connected', name = 'Hidden_layer', **features):
    weight = np.array([i for i in np.random.rand(num_neurons * num_neurons)]).reshape(num_neurons, num_neurons)
    if edges == 'fully_connected' or edges == None:
        return {'weight': weight, 'info': {'num_neurons': num_neurons, 'edges': edges, 'activationFun': activationFun, 'name': name}}
    if edges == 'partial':
        return {'weight': weight, 'info': {'num_neurons': num_neurons, 'edges': edge, 'activationFun': activationFun, 'name': name}}
    
    
def Output(num_neurons, activationFun, edges = 'fully_connected', name = 'Output_layer', **features):
    weight = np.array([i for i in np.random.rand(num_neurons)]).reshape(num_neurons, 1)
    if edges == 'fully_connected' or edges == None:
        return {'weight': weight, 'info': {'num_class': num_neurons, 'edges': edges, 'activationFun': activationFun, 'name': name}}
    if edges == 'partial':
        return {'weight': weight, 'info': {'num_class': num_neurons, 'edges': edge, 'activationFun': activationFun, 'name': name}}
    
    
