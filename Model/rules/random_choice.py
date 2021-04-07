import numpy as np

def random_choice(P):
    A = np.unique(P)
    return np.random.choice(A)