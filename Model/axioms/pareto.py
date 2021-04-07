import numpy as np
from util import voters_preference_x_over_y

def pareto(P, f):
    A = np.unique(P)
    n, m = P.shape
    for x in f:
        for y in A:
            if x == y:
                continue
            if voters_preference_x_over_y(y, x, P) == n:
                return False
    return True