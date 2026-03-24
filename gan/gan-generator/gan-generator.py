import numpy as np

def generator(z: np.ndarray, output_dim: int) -> np.ndarray:
    """
    Generate fake data from noise vectors.
    """
    # Your implementation here
    bs, noisedim = z.shape
    w = np.random.randn(noisedim, output_dim)*0.01
    b = np.zeros((1, output_dim))
    fake = np.tanh(z @ w + b)

    return fake