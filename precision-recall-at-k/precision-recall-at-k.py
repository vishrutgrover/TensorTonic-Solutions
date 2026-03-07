def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    rec = recommended[:k]
    hits = len(set(relevant).intersection(set(rec)))
    return [hits/k, hits/len(relevant)]