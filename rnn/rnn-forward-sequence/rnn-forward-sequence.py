import numpy as np

def rnn_forward(X: np.ndarray, h_0: np.ndarray,
                W_xh: np.ndarray, W_hh: np.ndarray, b_h: np.ndarray) -> tuple:
    """
    Forward pass through entire sequence.
    """
    # YOUR CODE HERE
    T = X.shape[1]
    h_t = h_0
    hidden_states = []

    for t in range(T):
        x_t = X[:, t, :] # (batch, input_size)
        h_t = np.tanh(h_t @ W_hh.T + x_t @ W_xh.T + b_h)  # (batch, hidden_size)
        hidden_states.append(h_t)

    H_all = np.stack(hidden_states, axis=1) # (batch, T, hidden_size)
    return H_all, h_t