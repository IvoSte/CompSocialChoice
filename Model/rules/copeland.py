import numpy as np
import rules.util

def copeland(P):
    """ 
    Rule:
    Copeland(P) = argmax (x in A) { C_P(x) }

    where

    C_p(x) = len({y in A | x net > y}) - len({y in A | y net > x}) 
    """
    copeland_scores = {key:0 for key in np.unique(P)}
    for ballot in P:
        for x in ballot:
            copeland_scores[x] = copeland_score(x, P)
    print(copeland_scores)
    highest_score = copeland_scores[max(copeland_scores, key=copeland_scores.get)]
    return set([x for x in np.unique(P) if highest_score == copeland_scores[x]])
    
# c - a : 2
# a - c : 2

# c - b : 3
# b - c : 1

# b - a: 1 
# a - b: 3

# b - c: 1
# c - b: 3

def copeland_score(x, P):
    """
    Copeland score CP(x) = |{y in A | x net y}| - |{y in A | y net x}}
    """
    A = np.unique(P)
    score = 0
    for y in A:
        count_a, count_b = rules.util.pairwise_comparison_preference(x, y, P)
        if count_a == count_b:
            continue
        score += 1 if count_a > count_b else -1
    return score
