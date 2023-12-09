/*
y = wx => sop
Error: have problem variable loosing their value after multiple function call
*/


#include<iostream>
#include<math.h>

class Neuron{
  static float x;
  static float real;
  static float learning_rate;
  static float w;
  static float sop;
  
public:
  Neuron(float x, float real, float learning_rate, float w){
     x = x;
     real = real;
     learning_rate = learning_rate;
     w = w;
     sop = w * x;
   }
  float error(float *predicted){
    return pow(((*predicted) - real), 2);
  }
  float sigmoid(){
    return 1.0 / ( 1 + exp(-1 * sop));
  }
  float error_prediction_deriv(float *predicted){
    return 2 * ((*predicted) - real);
  }
  float prediction_sop_deriv(){
    return sigmoid() * (1.0 - sigmoid());
  }
  float sop_w_deriv(){
    return x;
  }
  void update_w(float *grad){
    w = w - (learning_rate * (*grad));
    sop = w * x;
  }
};

int main()
{
  //Creating nueron
  Neuron *n = new Neuron(2.0, 1.0, 0.01, 0.5);
    
  short int epochs;
  std::cout << "Enter epochs: ";
  std::cin >> epochs;
  for(int i = 0; i < epochs; i++){
    //Forward pass
    float *predicted = new float(n->sigmoid());
    float *err = new float(n->error(predicted));
    std::cout << "Prediction: " << *predicted << ", Error: " << *err << std::endl;
      
    //Backward pass
    float *g1 = new float(n->error_prediction_deriv(predicted));
    float *g2 = new float(n->prediction_sop_deriv());
    float *g3 = new float(n->sop_w_deriv());

    float *grad = new float((*g1) * (*g2) * (*g3));
    n->update_w(grad); //updating weight
      
    delete predicted;
    delete err;
    delete g1;
    delete g2;
    delete g3;
    delete grad;
  }
    
  return 0;
}
