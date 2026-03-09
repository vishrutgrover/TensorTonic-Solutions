import numpy as np

def rmsprop_step(w, g, s, lr=0.001, beta=0.9, eps=1e-8):
    """
    Perform one RMSProp update step.
    """
    # Write code here
    w, g, s = np.array(w), np.array(g), np.array(s)
    news = beta*s+ (1-beta)*(g*g)
    neww = w-(lr*g)/(np.sqrt(news+eps))
    return neww, news