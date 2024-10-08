"""
Very simple feedforward NN

Input-Layer:
    3-Dimensional Input layer

Hidden-Layer:
    One neuron

Output-Layer:
    1-Dimensional Output layer

Initializing of values:
    W uses the Xavier Initialization to create an initial value for the weights
    W ∼ N(0, 2/(n_in + n_out))
    n_in is the number of input features and
    n_out is the number of neurons in the layer
    N is the normal distribution function


Forward Propagation:
    Z = W * X + b

Activation Function:
    Sigmoid: A = 1/(1+e^-Z)
    ReLU A = max(0, 7)

Loss Function:
    L = 1/2 * (A - Y)^2

Backpropagation:
    Derivatives:
        dL/dA = (A - Y)
        dA/dZ = A(1 - A)
        dZ/dW = X
        dZ/db = 1

    Chain rule:
        dL/dW = dL/dA * dA/dZ * dZ/dW = (A − Y) * A(1 − A) * X
        dL/db = dL/dA * dA/dZ * dZ/db = (A − Y) * A(1 − A)

    Gradient Descent:
        W = W - n * dL/dW
        b = b - n * dL/db
        where n ist the learning rate
"""


import numpy as np


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def feedforward_nn(epochs, x, y):
    n_in = 3
    n_out = 1
    w = np.random.normal(0, np.sqrt(2 / (n_in + n_out)), size=(n_in, n_out))
    b = 0
    learning_rate = 0.005
    for epoch in range(epochs):
        z = np.dot(w.T, x) + b
        a = sigmoid(z)

        dl_dw = (a - y) * a * (1 - a) * x
        dl_db = (a - y) * a * (1 - a)

        w = w - learning_rate * dl_dw
        b = b - learning_rate * dl_db

        if epoch % 100 == 0:  # Every 100 epochs print the current values
            print(f"Epoch {epoch}: w = {list(map('{:.3f}%'.format, w.flatten()))}, b = {list(map('{:.3f}%'.format,b))}, loss = {list(map('{:.3f}%'.format,(a - y) ** 2))}")

    return w, b


def test_nn():
    x = np.array([0.1, 0.2, 0.7])
    y = np.array([0.5])

    epochs = 1000

    w, b = feedforward_nn(epochs, x, y)

    print(f"Final weights: {w.flatten()}")
    print(f"Final bias: {b}")


test_nn()

