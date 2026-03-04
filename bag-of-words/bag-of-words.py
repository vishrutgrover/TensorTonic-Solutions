import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    # Your code here
    d = {}
    for i in vocab: d[i]=0
    for i in tokens: 
        if i in d: d[i]+=1
    return np.asarray(list(d.values()), dtype=int)