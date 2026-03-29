import numpy as np

def impute_missing(X, strategy='mean'):
    """
    Fill NaN values in each feature column using column mean or median.
    """
    # Write code here
    X = np.array(X)
    out = X.copy()
    
    if X.ndim==1:
        nanmask = np.isnan(X)
        # print(nanmask)
        if np.any(~nanmask):
            if strategy=="mean": fill = np.mean(X[~nanmask])
            else: fill = np.median(X[~nanmask])
        else: fill = 0
        out[nanmask]=fill
        return out

    for col in range(X.shape[1]):
        colv = X[:,col]
        nanmask = np.isnan(colv)
        # print(nanmask)
        if np.any(~nanmask):
            if strategy=="mean": fill = np.mean(colv[~nanmask])
            else: fill = np.median(colv[~nanmask])
        else: fill = 0
        out[nanmask, col]=fill
    return out