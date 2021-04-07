from .util import count_max_choices
import numpy as np

def plurality_(P):
    # this works, but not defined enough.
    return {P[P[:,0].argmax(),0]}

def plurality(P):
    alt_top_choice = count_max_choices(P)
    social_choice = set()
    for x in alt_top_choice:
        a = True
        for y in alt_top_choice:
            if x != y and alt_top_choice[x] < alt_top_choice[y]:
                a = False            
                break
        if a:
            social_choice.add(x)
    return social_choice

