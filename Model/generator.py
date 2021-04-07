# Preference generator: generate set of preferences according to constraints,
#   Keep generating sets either randomly or brute force. 
import numpy as np
from helper import *



class Generator:
    """
    Brute force mode:
        The generator takes a max n and max m, for which it will generate all possible permutations
        of P/ sets of all linear orders.
        It does this by first generating a single ballot (base) of length m (alternatives)
        then it generates a table (heaps_table) of all permutations of that base using Heap's algorithm
        To produce a full P, we use a permutation vector of length n (voters)
        the index of this vector refers to the voter, the value to the permutation of ballot.
        Brute forcing all permutations, by counting incrementally on the vector (from 0 to n_permutations per index)
        e.g.:
        m = 3, n = 2
        base = ['a', 'b', 'c']
        heaps_table = 6 rows of all permutations
        permutation_vector = <0, 0> returns P = {['a', 'b', 'c'],['a', 'b', 'c']}
        permutation_vector = <0, 1> returns P = {['a', 'b', 'c'],['b', 'a', 'c']}
        ...until <5, 5>
        then it increases the parameters and starts over
     """

    def __init__(self, m, n, mode = "random", max_m = 2, max_n = 2, max_P = -1):
        """
        arguments:
            m = (start) value for number of alternatives (length of ballot/unique options)
            n = (start) value for number of voters (amount of ballots)
            mode = how to generate ballots, 
                arguments : 
                    "random"
                    "bruteforce"
            max_m = ceiling of number of alternatives for brute force
            max_n = ceiling of number of votes for brute force
            max_P = ceiling of number of preference sets for random generation, set to -1 for infinite
        """

        self.done = False
        self.mode = mode

        # boundaries
        self.max_m = max_m
        self.max_n = max_n
        self.max_P = max_P

        # current progress
        self.cur_m = m
        self.cur_n = n
        self.cur_num_P = 0

        self.heaps_table = []
        self.permutation_vector = []

        if mode == "bruteforce":
            self.init_brute_force()

    # Controls
    def reset(self):
        self.done = False
        self.cur_m = 1
        self.cur_n = 1
        self.cur_num_P = 0

    def is_done(self):
        """Basecase for random generator"""
        if self.cur_num_P == self.max_P:
            self.done = True
        return self.done

    def next(self):
        self.cur_num_P += 1
        if self.mode == "random":
            return self.random_preference_generator(self.cur_m, self.cur_n)
        elif self.mode == "bruteforce":
            return self.next_bruteforce()

    def generate_base(self, m,n):
        # Create ordinal values for single row
        p = np.arange(0, m, 1)

        # Alternatives are characters
        p = [int_to_char(a) for a in p]

        P = p
        # Create more rows of votes
        for _ in range(n-1):
            P = np.concatenate((P, p), axis = 0)
        P = np.reshape(P, (n, m))
        return P

    def generate_base_ballot(self, m):
        # Create ordinal values for single row
        p = np.arange(0, m, 1)

        # Alternatives are characters
        p = [int_to_char(a) for a in p]
        return p

    def random_preference_generator(self, m, n):
        """m = number of alternative, n = number of voters""" 

        # Shuffle order per row randomly
        P = randomize(self.generate_base(m, n))
        return P

    def init_brute_force(self):
        #print("Initializing brute force mode")
        self.init_heaps_table(self.cur_m)
        self.init_permutation_vector(self.cur_n)

    def next_bruteforce(self):
        P = np.empty((0,self.cur_m))
        for i in self.permutation_vector:
            #print("Appending {}".format(self.heaps_table[i]))
            P = np.append(P, [self.heaps_table[i]], axis = 0)
        if not self.increment_permutation_vector():
            # if permutation vector is at the max, increase 
            self.increment_parameters()
            self.init_brute_force()
        return P

    def increment_parameters(self):
        print("current parameters: m {} n {}".format(self.cur_m, self.cur_n))
        if self.cur_m < self.max_m:
            self.cur_m +=1
        elif self.cur_n < self.max_n:
            self.cur_n += 1
        else :
            self.done = True

    def increment_permutation_vector(self):
        """Vector tracking which permutations are used per voter"""
        i = len(self.permutation_vector)-1
        # go to the last value that is not the max value
        while self.permutation_vector[i] == len(self.heaps_table)-1:
            if i == 0:
                return False    # vector completed, init next round of parameters
            i -= 1

        # increase current value
        self.permutation_vector[i] += 1
        # reset all tail values
        for j in range(i + 1, len(self.permutation_vector)):
            self.permutation_vector[j] = 0
        return True # Operation succesful

    def init_heaps_table(self, m):
        """Generate a table of all permutations of a single ballot with m alternatives"""
        base = self.generate_base_ballot(m)
        self.heaps_table = np.empty((0,m))
        self.heap_permutation(base,m)

    def heap_permutation(self, a, size):
        """Using Heap's recursive algorithm to generate all permutations"""
        if size == 1:
            self.heaps_table = np.append(self.heaps_table, [a], axis = 0)
            return
        
        for i in range(size):
            self.heap_permutation(a, size-1)
        
            if size & 1:
                a[0], a[size-1] = a[size-1], a[0]
            else:
                a[i], a[size-1] = a[size-1], a[i]

    def init_permutation_vector(self, n):
        self.permutation_vector = np.zeros((n,),dtype=int)