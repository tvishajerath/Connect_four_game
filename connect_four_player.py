# connect_four_player.py
#
# A Connect-Four Player class  

from connect_four_board import Board

class Player:
    """ A Connect Four player. """

    def __init__(self, checker):
        """ Constructs a new Player object. """
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0

    def __repr__(self):
        """ Returns a string representation of the player. """
        return "Player " + self.checker

    def opponent_checker(self):
        """ Returns a one-character string representing the opponent's checker. """
        return 'O' if self.checker == 'X' else 'X'

    def next_move(self, b):
        """ Accepts a Board object `b` and returns the column where the player wants to move. """
        while True:
            try:
                col = int(input("Enter a column: "))
                if b.can_add_to(col):
                    self.num_moves += 1
                    return col
                else:
                    print("Try again!")
            except ValueError:
                print("Invalid input. Please enter an integer.")
