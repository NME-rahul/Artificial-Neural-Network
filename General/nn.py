import evaluation

def create(layers): #it is working like array of every weights.
    return layers

def fit(model, input_data, epochs, num_class, learning_rate, target):
    result = {'forwardPropgation': [], 'backwardPropgation': []}
    result['forwardPropgation'] = evaulation.forwardPropgation(model, data, epochs, num_cass, target)
    #result['backwardPropgation'] = evaluation.backwardPropogation(model, epochs, num_class, learning_rate)
    return result
        
def summary(model):
   print('total paramenters: ', model[0])
