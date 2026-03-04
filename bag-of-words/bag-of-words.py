import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    # Your code here
    # d = {}
    # for i in vocab: d[i]=0
    # for i in tokens: 
    #     if i in d: d[i]+=1
    # return np.asarray(list(d.values()), dtype=int)

    tokens = np.array(tokens)
    vocab = np.array(vocab)
    unique, counts = np.unique(tokens, return_counts=True)
    count_map = dict(zip(unique, counts))
    return np.array([count_map.get(word, 0) for word in vocab], dtype=int)