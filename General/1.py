import numpy as np
import nn
import evaluation
import layers


target = [2];

data = np.array([i for i in np.random.rand(3)]).reshape(3, 1)
            
model = 0
            
model = nn.create([
    layers.Input(num_inputs = 3, activationFun = 'sigmoid', name = 'Input'),
        
    layers.Hidden(num_neurons = 3, edges = 'fully_connected', activationFun = 'sigmoid', name = 'Hidden_layer_1'),
        
    layers.Output(num_neurons = 3, activationFun = 'sigmoid', name = 'Output')
    ])

print(model)

#nn.summary(model = model)
#prediction = nn.fit(model = model, input_data = data, epochs = 10, num_class = 1, learning_rate = 0.01, target = target) #[predcicton, error]

#print(prediction['forwardPropgation'])               