import numpy as np

def batch_norm_forward(x, gamma, beta, eps=1e-5):
    """
    Forward-only BatchNorm for (N,D) or (N,C,H,W).
    """
    # Write code here
    # x = np.array(x)
    # mu = np.sum(x, keepdims=True, axis = 0) / len(x)
    # sig = np.sum((x - mu)**2, keepdims= True, axis = 0) / len(x)
    # xcap = (x-mu)/(sig+eps)**0.5
    # # print(mu, sig, xcap)
    # if x.ndim == 2:
    #     gamma, beta = np.array(gamma), np.array(beta)
    #     gamma, beta = gamma.reshape(1, -1), beta.reshape(1,-1)
    
    # if x.ndim == 4: 
    #     gamma, beta = np.array(gamma), np.array(beta)
    #     gamma, beta = gamma.reshape(1, -1, 1, 1), beta.reshape(1,-1, 1, 1)
        
    # return gamma*xcap + beta

    import numpy as np

def batch_norm_forward(x, gamma, beta, eps=1e-5):
    x = np.array(x)

    if x.ndim == 2:
        # (N, D)
        mu = np.mean(x, axis=0, keepdims=True)
        var = np.var(x, axis=0, keepdims=True)

        xcap = (x - mu) / np.sqrt(var + eps)

        gamma = np.array(gamma).reshape(1, -1)
        beta = np.array(beta).reshape(1, -1)

    elif x.ndim == 4:
        # (N, C, H, W)
        mu = np.mean(x, axis=(0, 2, 3), keepdims=True)
        var = np.var(x, axis=(0, 2, 3), keepdims=True)

        xcap = (x - mu) / np.sqrt(var + eps)

        gamma = np.array(gamma).reshape(1, -1, 1, 1)
        beta = np.array(beta).reshape(1, -1, 1, 1)

    return gamma * xcap + beta