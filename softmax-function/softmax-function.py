import numpy as np

def softmax(x):
    """
    Compute the softmax of input x.
    Works for 1D or 2D NumPy arrays.
    For 2D, compute row-wise softmax.
    """
    # Write code here
    x = np.array(x)
    axis = 1 if x.ndim == 2 else 0
    shi = x - np.max(x, axis=axis, keepdims=True)
    ex = np.exp(shi)
    return ex / np.sum(ex, axis=axis, keepdims=True)