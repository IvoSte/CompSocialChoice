import numpy as np
import rules.util
import math

def elo_test(P):
    starting_elo = 1000
    K = 32
    ratings = {key:starting_elo for key in np.unique(P)}
    ratings_temp = {key:starting_elo for key in np.unique(P)}
    A = np.unique(P)
    for ballot in P:
        for a in A:
            ratings_temp[a] = calculate_elo_after_round(a, ballot, K, ratings)
        ratings = ratings_temp    # update scores only after a round
    print(ratings)
    return set(ratings.keys())
    #get all alternatives
    #per ballot
    #    loop over alternatives
    #        calculate rating
    #order by rating, return order
    
    # Test if the order of ballots matters. If not, good. If yes, see how to fix.

 # Change so its symmetric? Does not seem zero-sum yet, is it working properly?
 # How to ensure order does not matter? Needs to be fixed mathematically

def calculate_elo_after_round(a, B, K, ratings):
    expected_score = 0
    score = 0
    # Calculate expected and real scores
    for b in B:
        if b == a:
            continue
        expected_score += 1/(1 + math.pow(10,(ratings[b] - ratings[a])/400))       # Domain = [0, 1]
        score += rules.util.pairwise_winner(a, b, B)
    print("{} {}".format(score, expected_score))
    new_rating = ratings[a] + (K * (score - expected_score))
    print("{} rating: {}, after: {}".format(a, ratings[a], new_rating))
    return new_rating