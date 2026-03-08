import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    # Write code here
    x = np.asarray(x)
    ex, emx = 2.718**x, 2.718**(-x)
    return (ex - emx)/(ex+emx)