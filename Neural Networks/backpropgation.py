#add normalization layer
import errors

class BackPropogation:
  def __init__(self, learning_rate):
    self.learning_rate = learning_rate

  def error_prediction_deriv(prediction, y): #1
    return -2 * (y - prediction)

  def prediction_sop_deriv(activation, prediction): #2
    if activation.lower() == 'sigmoid':
      return (prediction) * (1.0 - prediction)
    elif activation.lower() == 'rleu':
      return 0 if prediction <= 0 else 1
    elif activation.lower() == 'leaky_rleu':
      return 0.1*1 if prediction <= 0 else 1
    elif activation.lower() == 'identity':
      return 1
    elif activation.lower() == 'tanh':
      return (prediction + 1)**2 - (2*(prediction + 1))

  def sop_weight_deriv(prediction): #3
    return prediction

  def sop_prediction_deriv(weight): #4
    return weight

  def col_prod(self, arr1, arr2):
    for col in range(arr1.shape[1]):
      arr2 = arr2 * arr1[:, col][:, np.newaxis]
    return arr2

  def find_derivs(self, previous_layer_weight, prediction, activation, save):
    derivs = [sop_prediction_deriv(previous_layer_weight), prediction_sop_deriv(activation, prediction), sop_weight_deriv(prediction)]
    save = self.col_prod(save, derivs[0])
    save = save.T * derivs[1]
    gradient = self.col_prod(save, derivs[2])
    return gradient, save

  def update_weight(self, weight, gradient):
    return weight - self.learning_rate * gradient

  def last_layer(self, prediction, activation, actual):
    derivs = [error_prediction_deriv(predictions[-1], actual), prediction_sop_deriv(activation, prediction), sop_weight_deriv(prediction)]
    save = derivs[0]
    save = self.col_prod(save, derivs[1])
    gradient = self.col_prod(save, derivs[2])
    return gradient, save

  def __call__(self, weights, predictions, activations, actual):
    gradient, save = self.last_layer(predictions[-1], activations[-1], actual)
    weights[-1] = self.update_weight(weights[-1], gradient)
    previous_layer_weight = weights[-1]

    num_layers = len(weights)

    if num_layers > 1:
      for layer in range(1, num_layers+1):
        gradient, save = self.find_derivs(previous_layer_weight, predictions[-layer], activations[-layer], save)
        previous_layer_weight = weights[-layer]
        weights[-layer] = self.update_weight(weights[-layer], gradient)
    return weights
