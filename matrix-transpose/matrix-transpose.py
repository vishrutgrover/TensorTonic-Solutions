import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    M, N = len(A), len(A[0])
    x = np.zeros((N,M))
    for i in range(M):
        for j in range(N): x[j][i] = A[i][j]
    return x