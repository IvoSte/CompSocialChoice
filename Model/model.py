from scf import SCF
from rules.condorcet import condorcet
from rules.dictatorship_i import dictatorship_i
from rules.plurality import plurality
from rules.copeland import copeland
from rules.elo_test import elo_test
from rules.random_choice import random_choice
from axioms.unanimous import unanimous
from axioms.resolute import resolute
from generator import Generator
from axiom import Axiom
import numpy as np
from helper import *

#A = ['a','b','c','d','e']

# P = numpy array where rows = voter preference, columns = order of alternative preference
def preference_generator(m, n):
    """m = number of alternative, n = number of voters""" 

    # Create ordinal values for single row
    p = np.arange(0, m, 1)

    # Alternatives are characters
    p = [int_to_char(a) for a in p]

    P = p
    # Create more rows of votes
    for _ in range(n-1):
        P = np.concatenate((P, p), axis = 0)
    P = np.reshape(P, (n, m))

    # Shuffle order per row randomly
    P = randomize(P)
    return P

def main():
    # P = preference_generator(2, 3)
    # print("Preferences P:")
    # print(P)
    f_rng = SCF("Random Choice", random_choice)
    #f_con = SCF("Condorcet", condorcet)
    f_plur = SCF("Plurality", plurality)
    g = Generator(2,2,mode = "bruteforce",max_m = 4, max_n = 3)
    a = Axiom("resolute", resolute)
    a.check_axiom(g, f_plur)
    

    #f_dict = SCF("Dictatorship", dictatorship_i)
    #f_cond = SCF("Condorcet", condorcet)
    #f_cope = SCF("Copeland", copeland)
    #f_elo = SCF("ELO rating", elo_test)
    #f = f_plur.apply_rule(P)
    #f = f_rng.apply_rule(P)
    #print(f)
    #print(unanimous(P, f))
    #print(f_dict.apply_rule_arg(1, P))
    #print(f_cond.apply_rule(P))   
    #print(f_cope.apply_rule(P))
    #print(f_elo.apply_rule(P))


if __name__ == "__main__":
    main()



# Goals: 
# I want to generate votes/preferences
# I want SCF, that take a set P of preferences as input and give a SC as output
# I also want SPF, taking P as input, but giving ranked preferences as output
# I want constraint functions, that show if a set P and SCF f with result SC adhere to the rule
# I then want a generator of votes
# I then want a function that generates votes and patterns and runs them through the SCF and constraints, to show if they adhere.