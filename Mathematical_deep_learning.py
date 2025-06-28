#writing clean modular functions

import numpy as np

#Activation functions 
def sigmoid(z):
    return 1 / (1 + np.exp(-z)) #this callculates the power of Z

def relu(z):
    return np.maximum(0, z) # returns z if z > 0, otherwise 0

def relu_derivative(z):
    return (z > 0).astype(float) #this is backpropagation

def forward_propagation(X, W1, b1, W2, b2):
    z1 = np.dot(W1, X) + b1 #does the matrix multiplcation between weights and inputs, aslo adds a bias to shift activation
    A1 = relu(z1) #activated output from layer 1
    z2 = np.dot(W2, A1) + b2
    A2 = sigmoid(z2) #predicted probability after sigmoid
    cache = (z1,A1,z2,A2) 
    return A2, cache

def loss_function(A2, Y):
    m = Y.shape[1]
    loss = -np.sum(Y * np.log(A2) + (1-Y) * np.log(1 -A2))/m #penalises wromg predictions with logs
    return loss

def backward_propagation(X, Y, cache, W2):
    m = X.shape[1]
    z1, A1, z2, A2 = cache

    #the error at the output layer
    dz2 = A2 - Y #this is the difference between prediction and true labels ie error signal and output
    dW2 = np.dot(dz2, A1.T) / m #this is the gradient for w2
    db2 = np.sum(dz2, axis = 1, keepdims= True)/m #this is the gradient for b2

    dA1 = np.dot(W2.T, dz2) #propagate the error back to the hiddden layer
    dz1 = dA1 * relu_derivative(z1)

    dW1 = np.dot(dz1, X.T) / m #this is the gradient for w1
    db1 = np.sum(dz1, axis = 1, keepdims= True)/m
    
    grads = {"dW1": dW1, "db1": db1, "dW2": dW2, "db2": db2}
    return grads

def update_parameters (W1, b1, W2, b2, grads, lr): #adjust the weights and biases by stepping against the gradient to reduce loss.
    W1 -= lr * grads['dW1']
    b1 -= lr * grads['db1']
    W2 -= lr * grads['dW2']
    b2 -= lr * grads['db2']
    
    return W1, b1, W2, b2


np.random.seed(42)
input_size = 5
hidden_size = 16
output_size = 1
m = 100

X = np.random.randn(input_size, m)
Y = np.random.randint(0, 2, size=(1, m)).astype(float)

W1 = np.random.randn(hidden_size, input_size) * 0.01
b1 = np.zeros((hidden_size, 1))
W2 = np.random.randn(output_size, hidden_size) * 0.01
b2 = np.zeros((output_size, 1))

lr = 0.01
epochs = 1000

losses = []
accuracies = []

for i in range(epochs):
    A2, cache = forward_propagation(X, W1, b1, W2, b2)
    loss = loss_function(A2, Y)
    grads = backward_propagation(X,Y, cache, W2)
    W1,b1,W2, b2 = update_parameters(W1,b1,W2, b2, grads, lr)

    predictions = (A2 > 0.5).astype(float)
    accuracy = np.mean(predictions == Y)

    losses.append(loss)
    accuracies.append(accuracy)
    if i % 100 == 0:
        print(f'Epoch {i}, loss: {loss:.4f}')

import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))

#plot the loss
plt.subplot(1,2,1)
plt.plot(losses, label = 'Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Loss Over Time')
plt.legend()

#plot Accuracy
plt.subplot(1,2,2)
plt.plot(accuracies, label = 'Accuracy', color = 'green')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.title('Accuracy Over Time')
plt.legend()

plt.tight_layout()
plt.show()
