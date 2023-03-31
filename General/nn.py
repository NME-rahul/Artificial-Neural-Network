import evaluation

def create(layers): #it is working like array of every weights.
    return layers

def fit(model, input_data, epochs, num_class, learning_rate, target):
    result = {'forwardPropgation': [], 'backwardPropgation': []}
    result['forwardPropgation'] = evaulation.forwardPropgation(model, data, epochs, num_cass, target)
    #result['backwardPropgation'] = evaluation.backwardPropogation(model, epochs, num_class, learning_rate)
    return result
        
def summary(model):
   cnt = 0; total = 0
   
   cnt = len(model[0]['weight'][:,0]) * len(model[0]['weight'][0])
   print('Trainable parameters in input layer: %d \nNumber of inputs: %d' %(cnt , model[0]['info']['num_inputs']))
   
   total = cnt; cnt = 0
   for i in range(1, len(model) - 1):
       cnt = cnt + (len(model[i]['weight'][0]) * len(model[i]['weight'][:,0]))
      
   print('\nNumber of Hidden layer: %d \nTrainable parameters in hidden layer: %d \nedges: %s ' %(len(model) - 2, cnt, model[1]['info']['edges']) )
   
   total = total + cnt; cnt = 0
   cnt = model[-1]['info']['num_class']
   print('\nNumber of class: %d \nedges: %s' %(cnt , model[-1]['info']['edges']))
   total = total + cnt
   
   print('\nTotal trainaable prameters: ',total)
