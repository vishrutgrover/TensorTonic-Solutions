import numpy as np

def normalize_3d(v):
    """
    Normalize 3D vector(s) to unit length.
    """
    # Your code here
    v = np.array(v)
    return v / np.maximum(np.sum(v**2, axis=-1, keepdims=True)**0.5, 1e-12)