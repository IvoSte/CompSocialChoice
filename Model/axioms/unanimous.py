import numpy as np

def unanimous(P, f):
    unique = np.unique(P[:,0])
    if len(unique) == 1 and set(unique[0]) != f:
        return False
    else :
        return True        
    