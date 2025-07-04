# connect_four_ai.py
#
# AI Player for use in Connect Four

import random
from connect_four_game import Player
from connect_four_board import Board

class AIPlayer(Player):
    def __init__(self, checker, tiebreak, lookahead):
        """ Constructs a new AIPlayer object. """
        assert checker in ['X', 'O']
        assert tiebreak in ['LEFT', 'RIGHT', 'RANDOM']
        assert lookahead >= 0

        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead

    def __repr__(self):
        """ Returns a string representation of the AIPlayer. """
        return f'Player {self.checker} ({self.tiebreak}, {self.lookahead})'

    def max_score_column(self, scores):
        """ Returns the index of the column with the max score, resolving ties using tiebreak strategy. """
        max_score = max(scores)
        best_cols = [i for i in range(len(scores)) if scores[i] == max_score]

        if self.tiebreak == 'LEFT':
            return best_cols[0]
        elif self.tiebreak == 'RIGHT':
            return best_cols[-1]
        elif self.tiebreak == 'RANDOM':
            return random.choice(best_cols)

    def scores_for(self, b):
        """ Computes scores for each column of board `b`. """
        scores = [50] * b.width

        for col in range(b.width):
            if not b.can_add_to(col):
                scores[col] = -1
            else:
                b.add_checker(self.checker, col)

                if b.is_win_for(self.checker):
                    scores[col] = 100
                elif self.lookahead == 0:
                    scores[col] = 50
                else:
                    opponent = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                    opp_scores = opponent.scores_for(b)
                    max_opp_score = max(opp_scores)

                    if max_opp_score == 0:
                        scores[col] = 100
                    elif max_opp_score == 100:
                        scores[col] = 0
                    else:
                        scores[col] = 50

                b.remove_checker(col)
        return scores

    def next_move(self, b):
        """ Returns the best move based on calculated scores. """
        self.num_moves += 1
        scores = self.scores_for(b)
        return self.max_score_column(scores)
