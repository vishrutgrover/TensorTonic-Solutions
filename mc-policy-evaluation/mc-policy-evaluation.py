import numpy as np
from collections import defaultdict
def mc_policy_evaluation(episodes, gamma, n_states):
    """
    Returns: V (NumPy array of shape (n_states,))
    """
    # Write code here
    dic = defaultdict(list)

    for wo in episodes:
        runs = 0
        returns = [0]*len(wo)

        # compute returns
        for i in range(len(wo)-1, -1, -1):
            k, v = wo[i]
            runs = v + gamma * runs
            returns[i] = runs

        # first-visit
        seen = set()
        for i, (k,_) in enumerate(wo):
            if k not in seen:
                seen.add(k)
                dic[k].append(returns[i])

    V = np.zeros(n_states)
    for k in dic: V[k] = sum(dic[k])/len(dic[k])
    return V