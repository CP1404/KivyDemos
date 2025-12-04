"""Tic Tac Toe game."""


class GameError(Exception):
    """Exception class for game error."""
    pass


class TicTacToeGame:
    """Game class for Tic Tac Toe."""

    def __init__(self):
        """Initialise game object with default board and first move."""
        self.next_move = 'X'
        self.board = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]

    def __str__(self):
        """Return string representation of game."""
        return "\n".join((str(row) for row in self.board))

    def make_move(self, row, column):
        """Make a move using row and column."""
        try:
            self.board[row][column] = self.next_move
            self.next_move = 'X' if self.next_move == 'O' else 'O'
            return self.board[row][column]
        except IndexError as e:
            raise GameError(f'Invalid move {row} {column}') from e

    def is_over(self):
        """Determine if game is over."""
        return self._is_line() or self._is_line(swapped=True) \
            or self._is_diagonal() or self._is_diagonal(swapped=True)

    def _is_line(self, swapped=False):
        """Determine if board state includes a horizontal or vertical line of the same tokens."""
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

    def _is_diagonal(self, swapped=False):
        """Determine if board state includes a diagonal line of the same tokens."""
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
