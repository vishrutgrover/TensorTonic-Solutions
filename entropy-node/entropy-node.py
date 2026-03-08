import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    _, counts = np.unique(y, return_counts=True)
    probs = counts/counts.sum()
    return -np.sum(probs*np.log2(probs))