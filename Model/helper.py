import numpy as np

def int_to_char(n):
    return chr(n+97)

def randomize(P):
    for idx, value in enumerate(P):
        np.random.shuffle(value)
    return P