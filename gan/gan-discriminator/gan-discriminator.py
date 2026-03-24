import numpy as np

def discriminator(x: np.ndarray) -> np.ndarray:
    """
    Classify inputs as real or fake.
    """
    # Your implementation here
    out, wei = x.shape
    W = np.random.randn(wei, 1) * 0.01
    b = np.zeros((1, 1))
    sig = 1/ (1+ np.exp(-(x @ W + b)))
    return sig