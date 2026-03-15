def lag_features(series, lags):
    """
    Create a lag feature matrix from the time series.
    """
    # Write code here
    mlag = max(lags)
    res = []
    for i in range(mlag, len(series)):
        r = [series[i-lag] for lag in lags]
        res.append(r)
    return res