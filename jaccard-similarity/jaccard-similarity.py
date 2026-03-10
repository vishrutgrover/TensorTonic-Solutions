def jaccard_similarity(set_a, set_b):
    """
    Compute the Jaccard similarity between two item sets.
    """
    # Write code here
    uni, inter = len(set(set_a).union(set(set_b))), len(set(set_a).intersection(set(set_b)))
    if uni ==0: return 0
    return inter/uni