/*
y = w * x => sop
*/

#include<bits/stdc++.h>

class Neuron{
  long x;
  long real;
  long learning rate;
  long w;
public:
  long sop = w * x;
  
  Neuron(long x, long real, long learning_rate, long w){
     long x = x;
     long real = real;
     long learning rate = learning_rate;
     long w = w;
   }
  long error(long predicted){
    return pow((predicted - real), 2);
  }
  long sigmoid(){
    return 1.0 / ( 1 + exp(-1 * sop));
  }
  long error_prediction_deriv(long predicted){
    return 2 * (predicted - real);
  }
  long prediction_sop_deriv(long sop){
    return sigmoid(sop) * (1.0 - sigmoid(sop));
  }
  long sop_w_deriv(){
    return x;
  }
  long update_weight(grad){
    w = w - (learning_rate * grad);
  }
};

int main()
{
  //Creating nueron
  Neuron *n = new Neuron(2.0, 1.0, 0.01, 0.5);
    
  short int epochs;
  cin >> epochs;
  for(int i = 0; i < epochs; i++){
    //Forward pass
    long *predicted = new long(n->sigmoid());
    long *err = new long(n->error(predicted));
    std::cout << "Prediction: " << predicted << ", Error: " << err << std::endl;
    //Backward pass
    long *g1 = new long(n->error_prediction_deriv(predicted));
    long *g2 = new long(n->prediction_sop_deriv());
    long *g3 = new long(n->sop_w_deriv());
    
    long *grad = new long(g1 * g2 * g3);
    n->update_w(grad); //updating weight
  }
  
  delete predicted;
  delete err;
  delete g1;
  delete g2;
  delete g3;
  delete grad;
  return 0;
}
