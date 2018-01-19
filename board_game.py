"""Tic Tac Toe game."""


class GameError(Exception):
    pass


class TicTacToeGame:
    def __init__(self):
        self.next_move = 'X'
        self.board = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]

    def __str__(self):
        return "\n".join((str(row) for row in self.board))

    def make_move(self, row, column):
        try:
            self.board[row][column] = self.next_move
            self.next_move = 'X' if self.next_move == 'O' else 'O'
            return self.board[row][column]
        except IndexError:
            raise GameError('invalid move {} {}'.format(row, column))

    def is_over(self):
        return self._check_line() or self._check_line(swapped=True) \
               or self._check_diagonal() or self._check_diagonal(swapped=True)

    def _check_line(self, swapped=False):
        for row in range(3):
            tally_crosses = 0
            tally_naughts = 0
            for column in range(3):
                if swapped:
                    i, j = column, row
                else:
                    i, j = row, column
                if self.board[i][j] == 'X':
                    tally_crosses += 1
                elif self.board[i][j] == 'O':
                    tally_naughts += 1
            if tally_crosses == 3 or tally_naughts == 3:
                return True
        return False

    def _check_diagonal(self, swapped=False):
        tally_crosses = 0
        tally_naughts = 0
        for row in range(3):
            if swapped:
                i, j = 2 - row, row
            else:
                i, j = row, row
            if self.board[i][j] == 'X':
                tally_crosses += 1
            elif self.board[i][j] == 'O':
                tally_naughts += 1
        if tally_crosses == 3 or tally_naughts == 3:
            return True
        return False
