import numpy as np

def Input(num_inputs, activationFun, **features):
    weight = np.array([i for i in np.random.rand(num_inputs * num_inputs)]).reshape(num_inputs, num_inputs)
    if 'name' not in features:
        features['name'] = 'Input'
    return {'weight': weight, 'info': {'num_inputs': num_inputs, 'activationFun': activationFun, 'name': features['name']}}
        
        
def Hidden(num_neurons, activationFun, **features):
    weight = np.array([i for i in np.random.rand(num_neurons * num_neurons)]).reshape(num_neurons, num_neurons)
    if 'name' not in features:
        features['name'] = 'Input'
    elif 'edges' not in features:
        features['edges'] = 'fully_connected'
    if features['edges'] == 'fully_connected' or features['edges'] == None:
        return {'weight': weight, 'info': {'num_neurons': num_neurons, 'edges': features['edges'], 'activationFun': activationFun, 'name': features['name']}}
    if features['edges'] == 'partial':
        return {'weight': weight, 'info': {'num_neurons': num_neurons, 'edges': features['edges'], 'activationFun': activationFun, 'name': features['name']}}
    
    
def Output(num_neurons, activationFun, **features):
    weight = np.array([i for i in np.random.rand(num_neurons)]).reshape(num_neurons, 1)
    if 'name' not in features:
        features['name'] = 'Input'
    elif 'edges' not in features:
        features['edges'] = 'fully_connected'
    if features['edges'] == 'fully_connected' or features['edges'] == None:
        return {'weight': weight, 'info': {'num_class': num_neurons, 'edges': features['edges'], 'activationFun': activationFun, 'name': features['name']}}
    if features['edges'] == 'partial':
        return {'weight': weight, 'info': {'num_class': num_neurons, 'edges': features['edges'], 'activationFun': activationFun, 'name': features['name']}}
    