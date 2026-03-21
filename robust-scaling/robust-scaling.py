def robust_scaling(values):
    """
    Scale values using median and interquartile range.
    """
    # Write code here
    orig = np.array(values)
    x = np.array(sorted(values))
    med = np.median(x)
    N = len(x)
    if N == 1: return np.zeros(N)
    q1 = np.median(x[:N//2])
    q3 = np.median(x[(N+1)//2:])
    print(med, q1, q3)
    if q3-q1 == 0: return np.zeros(N)
    return (orig-med)/(q3-q1)