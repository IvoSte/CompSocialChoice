import numpy as np

# When writing the rules, DO NOT care about computation time. Take them literally from the definition. Efficiency is NOT important.
# Readability / Logic is the main focus, not programming skills. Wrap things in logic functions when used more than twice

def alternatives_in_P(P):
    return np.unique(P)

def count_max_choices(P):
    unique, counts = np.unique(P[:,0], return_counts = True)
    return dict(zip(unique, counts))

def max_choice(A):
    return A[0]

def pairwise_comparison_preference(a, b, P):
    count_a = 0
    count_b = 0
    for ballot in P:
        temp_a, temp_b = pairwise_comparison_ballot(a,b,ballot)
        count_a += temp_a
        count_b += temp_b
    return count_a, count_b

def pairwise_comparison_ballot(a, b, ballot):
    """Who wins pairwise comparison
    returns 1 for argument that wins and -1 for the losing argument.
    returns 0 for both if one or both are missing"""
    if not a in ballot or not b in ballot:
        return 0,0
    for e in ballot:
        if e == a:
            return 1, -1
        elif e == b:
            return -1, 1
    return 0, 0

def pairwise_winner(a, b, ballot):
    if not a in ballot or not b in ballot:
        print("Warning, returned a tie for pairwise winner when one or more alternatives are missing from the ballot.")
        return 0.5
    for e in ballot:
        if e == a:
            return 1
        if e == b:
            return 0
    return 0.5

def voters_preference_x_over_y(P, x, y):
    """returns the indices of the ballots who voted x over y"""
    p_xy = []
    for idx, ballot in enumerate(P):
        if pairwise_winner(x, y, ballot):
            p_xy.append(idx)
    return p_xy