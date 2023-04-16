def calculate_y(x1, x2, w1, w2, b):
    return ((x1 * w1) + (x2 * w2) + b)

def activation(y):
    if y > 0:
        return 1
    elif y == 0:
        return 0
    elif y < 0:
        return -1

def update_w(x1, x2, w1, w2, learning_rate, target):
    return [w1 + (learning_rate * target * x1), w2 + (learning_rate * target * x2)]

def update_b(b, learning_rate, target):
    return b + (learning_rate * target)
    
def main():
    learning_rate = 1
    w1 = 0; w2 = 0; b = 0;
    yin = 0; y = 0;
    
    x1 = [1, -1, 1, -1]
    x2 = [1, 1, -1, -1]
    target = [1, -1, -1, -1]
    
    for i in range(4):
        y = calculate_y(x1[i], x2[i], w1, w2, b)
        yin = activation(y)
        print("y: %2d  yin: %2d  target: %2d    w1: %2d  w2: %2d  b: %2d" %(y, yin, target[i], w1, w2, b))
        w1, w2 = update_w(x1[i], x2[i], w1, w2, learning_rate, target[i])
        b = update_b(b, learning_rate, target[i])

main()
