import numpy as np
import errors

class Model:
  def __init__(self, layer_objects):
    self.Batch_size = layer_objects[0].shape[0]
    self.input_shape = layer_objects[0].shape[1][0] #(batch_size, inputs_shape)
    self.add_weight(layer_objects[1:]) #(weight, activation)
    self.num_layers = len(layer_objects) - 1

  def add_weight(self, layer_objects):
    self.trainable = []; self.traiables_activation = []
    weight_shape = self.input_shape
    for i, obj in enumerate(layer_objects):
      weight, activation =  obj(weight_shape), obj.activation
      self.trainable.append(weight); self.traiables_activation.append(activation)
      weight_shape = self.trainable[i][0].shape[0]

  def feed_forward(self, activation, weight, x):
    arr_mul = weight * x.T
    sop = self.calc_sop(arr_mul)[:, np.newaxis]
    prediction = Activation(activation)(sop)
    return prediction

  def calc_sop(self, arr_mul):
    temp = np.array([])
    for i in range(arr_mul.shape[0]):
      sop = 0
      for j in range(arr_mul.shape[1]):
        sop += arr_mul[i][j]
      temp = np.append(temp, [sop])
    return temp

  def train(self, inputs, epochs, verbose):
    x, y = inputs
    if !Errors.data_cardinality(x, y):
      history = {'error':[]}
      for epoch in range(epochs):
        layer_predictions = []
        for i, weight in enumerate(self.trainable):
          layer_predictions.append(self.feed_forward(self.traiables_activation[i], weight, x))
          x = layer_predictions[i]
        history['error'].append((layer_predictions[-1] - y)**2) #shows only error still
        self.trainable = BackPropogation(self.learning_rate)(self.trainable, layer_predictions, self.traiables_activation, y)
        if verbose != 0:
          print('Epochs: %d\nError: %f' %(epoch+1, error))

    return history
