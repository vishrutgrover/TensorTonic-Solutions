import numpy as np
def k_means_centroid_update(points, assignments, k):
    """
    Compute new centroids as the mean of assigned points.
    """
    # Write code here
    pts, assn = np.asarray(points), np.asarray(assignments)
    d = pts.shape[1]
    cent = []
    
    for i in range(k):
        clpts = pts[assn==i]
        # print(clpts)
        if len(clpts)==0: cent.append([0.0]*d)
        else: cent.append(clpts.mean(axis=0).tolist())
    return cent