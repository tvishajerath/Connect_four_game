# connect_four_board.py
#
# A Connect Four Board class

class Board:
    """ A data type for a Connect Four board with arbitrary dimensions """   
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.slots = [[' '] * self.width for row in range(self.height)]

    def __repr__(self):
        s = ''
        for row in range(self.height):
            s += '|'
            for col in range(self.width):
                s += self.slots[row][col] + '|'
            s += '\n'
        s += '-' * (self.width * 2 + 1) + '\n'
        s += ' '
        for col in range(self.width):
            s += str(col % 10) + ' '
        s += '\n'
        return s

    def add_checker(self, checker, col):
        assert(checker == 'X' or checker == 'O')
        assert(0 <= col < self.width)
        row = 0
        while self.slots[self.height - row - 1][col] != ' ':
            row += 1
        self.slots[self.height - row - 1][col] = checker

    def reset(self):
        self.slots = [[' '] * self.width for row in range(self.height)]

    def add_checkers(self, colnums):
        checker = 'X'
        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)
            checker = 'O' if checker == 'X' else 'X'

    def can_add_to(self, col):
        if col < 0 or col >= self.width:
            return False
        for row in range(self.height):
            if self.slots[row][col] == ' ':
                return True
        return False

    def is_full(self):
        for col in range(self.width):
            if self.can_add_to(col):
                return False
        return True

    def remove_checker(self, col):
        for row in range(self.height):
            if self.slots[row][col] != ' ':
                self.slots[row][col] = ' '
                break

    def is_win_for(self, checker):
        assert(checker == 'X' or checker == 'O')
        return (self.is_horizontal_win(checker)
                or self.is_vertical_win(checker)
                or self.is_down_diagonal_win(checker)
                or self.is_up_diagonal_win(checker))

    def is_horizontal_win(self, checker):
        for row in range(self.height):
            for col in range(self.width - 3):
                if all(self.slots[row][col + i] == checker for i in range(4)):
                    return True
        return False

    def is_vertical_win(self, checker):
        for row in range(self.height - 3):
            for col in range(self.width):
                if all(self.slots[row + i][col] == checker for i in range(4)):
                    return True
        return False

    def is_down_diagonal_win(self, checker):
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                if all(self.slots[row + i][col + i] == checker for i in range(4)):
                    return True
        return False

    def is_up_diagonal_win(self, checker):
        for row in range(3, self.height):
            for col in range(self.width - 3):
                if all(self.slots[row - i][col + i] == checker for i in range(4)):
                    return True
        return False
