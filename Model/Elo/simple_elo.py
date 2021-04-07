import math
from player import Player
    
class Elo_module:

    def __init__(self, k):
        self.K = k

    def play(self, A, B, S_A, S_B):
        # Play a single round, two players, S are achieved scores 0:loss 1:win 0.5:draw
        print("\nRound {} : {}, {} : {}".format(A.name, S_A, B.name, S_B))
        E_A = self.expected_score(A.elo, B.elo)
        E_B = self.expected_score(B.elo, A.elo)
        A.update_elo(self.new_rating(A.elo, E_A, S_A, self.K))
        B.update_elo(self.new_rating(B.elo, E_B, S_B, self.K))

    def play_pairwise(self, ranking):
        # Play with pairwise elo calculation --> update elo's as if many 1v1 rounds are played
        print("\nRound {}".format([p.name for p in ranking]))
        players = list(ranking)
        # Store newly calculated elo values before updating
        elo_updates = {p.name : [] for p in ranking}
        for p in ranking:
            # don't play versus yourself or calculate the same matchup twice.
            players.remove(p)
            for other in players:
                E_p = self.expected_score(p.elo, other.elo)
                E_o = self.expected_score(other.elo, p.elo)
                S_p = 1 if ranking.index(p) > ranking.index(other) else 0
                S_o = 1 if ranking.index(p) < ranking.index(other) else 0
                elo_updates[p.name].append(self.new_rating(p.elo, E_p, S_p, self.K))
                elo_updates[other.name].append(self.new_rating(other.elo, E_o, S_o, self.K))
        # update elo values after all calculations
        for p in ranking:
            p.update_elo_multi(elo_updates[p.name])


    def play_multi(self, ranking):
        # Play a round and update elo according to expected and achieved ranking
        print("\nRound {}".format([p.name for p in ranking]))
        # calculate expected scores
        exp_score = self.multi_expected_scores(ranking)
        # update elos
        for rank, p in enumerate(ranking):
            S_p = (rank + 0.5)/len(ranking)
            print(S_p)
            p.update_elo(self.new_rating(p.elo, exp_score[p.name], S_p, self.K))

    def multi_expected_scores(self, players):
        # Calculate expected score for a 
        avg_rating = self.average_rating(players)
        expected_scores = {}
        for player in players:
            # average opponent score is average score without own score
            avg_opp_rating = (((avg_rating * len(players)) - player.elo) / (len(players)-1))
            expected_scores[player.name] = self.expected_score(player.elo, avg_opp_rating)
        return expected_scores

    def new_rating(self, R_A, E_A, S_A, K):
        return R_A + (K * (S_A - E_A))


    def expected_score(self, R_A, R_B):
        # Expected outcome of a round between Rating A and Rating B, for player A.
        expected = 1.0 / (1 + math.pow(10, (R_B - R_A)/400))
        return expected

    def average_rating(self, players):
        total = 0
        for player in players:
            total += player.elo
        return total/len(players)

def main():
    A = Player("A")
    B = Player("B")
    C = Player("C")
    D = Player("D")
    E = Player("E")
    F = Player("F")
    ELO = Elo_module(40)
    # for _ in range(3):
    #     E.play(A, B, 1, 0)
    #     print("Total : {}".format(A.elo + B.elo))
    for _ in range(3):
        ELO.play_multi([A, B, C])
        print("Total : {}".format(A.elo + B.elo + C.elo))

    for _ in range(3):
        ELO.play_pairwise([D, E, F])
        print("Total : {}".format(D.elo + E.elo + F.elo))


if __name__ == "__main__":
    main()


    # def calculate_elo_old(self, Ewin, Elose, Cwin, Close, startbonus):
    #     bonus = startbonus / math.pow(2,Cwin)
    #     scalar = 1 if Cwin == 0 or Close == 0 else Cwin / float(Close)
    #     Edelta = self.minElo + ((self.maxElo - self.minElo)/scalar)
    #     print("Bonus {} Edelta {}".format(bonus, Edelta))
    #     return (Ewin + (Edelta + bonus)), (Elose - (Edelta + bonus))