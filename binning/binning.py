import numpy as np
def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    # Write code here
    x = np.array(values)
    w = (np.max(x)-np.min(x))/num_bins
    lis = []
    if w == 0: 
        lis.extend([0]*len(values))
        return lis
    else: 
        wo = (x-np.min(x))/w
        for i in wo: lis.append(min(int(i), num_bins-1))
        return lis