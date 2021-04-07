class Player:

    def __init__(self, name, elo = 1000):
        self.name = name
        self.elo = 1000
        self.wins = 0
        self.losses = 0
        self.draw = 0
        self.history = []


    def play(self, other):
        pass

    def update_elo(self, new_elo):
        # update elo rating with the new rating
        print("{} :: {} --> {}".format(self.name, self.elo, new_elo))
        self.elo = new_elo

    def update_elo_multi(self, new_elos):
        # update player rating from set of changes, multiple pairwise matchup elo calculations from a single round
        for idx, new_elo in enumerate(new_elos):
            new_elos[idx] = new_elo - self.elo
        print(new_elos)
        self.update_elo(self.elo + sum(new_elos))

