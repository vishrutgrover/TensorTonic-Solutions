import numpy as np

def angle_between_3d(v, w):
    """
    Compute the angle (in radians) between two 3D vectors.
    """
    # Your code here
    v, w = np.array(v), np.array(w)
    den1, den2 = np.sum(v**2)**0.5, np.sum(w**2)**0.5
    if den1 == 0 or den2 == 0: return np.nan
    cost = np.clip((v@w) / (den1*den2), -1.0, 1.0)
    return np.arccos(cost)