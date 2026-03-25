import numpy as np

def angle_between_3d(v, w):
    """
    Compute the angle (in radians) between two 3D vectors.
    """
    # Your code here
    v, w = np.array(v), np.array(w)
    den1, den2 = np.sum(v**2)**0.5, np.sum(w**2)**0.5
    if den1 == 0: den1 = np.nan
    if den2 == 0: den2 = np.nan
    return np.clip(np.arccos((v@w) / (den1*den2)))