import numpy as np

def focal_loss(p, y, gamma=2.0):
    """
    Compute Focal Loss for binary classification.
    """
    # Write code here
    p, y = np.array(p), np.array(y)
    eps = 1e-12
    p = np.clip(p, eps, 1 - eps)
    tm1, tm2 = (1-p)**gamma * y * np.log(p), p**gamma*(1-y)*np.log(1-p)
    # print(tm1, tm2)
    return -np.sum(tm1+tm2)/len(tm1)