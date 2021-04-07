import numpy as np
from .util import pairwise_comparison_preference

def condorcet(P):
    """
    Rule: Condorcet(P) : {x} if for all y in A \{x}, x net P over Y
    Take the example:
    a b c
    b a c
    c b a

    a > c
    b > c
    b > a
    Condorcet winner:
    b
    """
    A = np.unique(P)
    highest_alternative = {key:0 for key in A}
    for (idx, x) in enumerate(A):
        if idx == len(A)-1:
            continue
        y = A[idx + 1]
        count_x, count_y = pairwise_comparison_preference(x, y, P)
        highest_alternative[x] += count_x
        highest_alternative[y] += count_y

    highest_alternative = {key:int(value/2) for (key, value) in highest_alternative.items()}
    return max(highest_alternative, key=highest_alternative.get)
    
