from sys import exit
from itertools import chain
import numpy as np
#matrix = np.arange(9).reshape(3, 3


NONE = '.'
RED = 'R'
YELLOW = 'Y'
FOUR = 4


class Game:
   def __init__ (self, cols = 7, rows = 6):
       """Create a new game."""
       self.cols = cols
       self.rows = rows
       self.board = [[NONE] * rows for _ in range(cols)]
       self.four_red = [RED] * FOUR
       self.four_yellow = [YELLOW] * FOUR

   def insert(self, column, color):
       """Insert the color in the given column."""
       c = self.board[column]
       if c[0] != NONE:
           raise Exception
       i = -1
       while c[i] != NONE:
           i -= 1
       c[i] = color

   def print_board(self):
       """Print the board."""
       print(' '.join(map(str, range(self.cols))))
       for y in range(self.rows):
           print(' '.join(str(self.board[x][y]) for x in range(self.cols)))
       print()

   def get_winner(self):
       # mirrir_board = [list(r[::1)]
       transposed_board = self.board.transpose()
       cols = self.board.tolist()
       rows = transposed_board.tolist()
       posdiag = [list(np.diagonal(self.board, i)) for i in range(-2, 3)]
       print(posdiag, '\n')
       negdiag = [list(np.diagonal(self.board.fliplr, i)) for i in range(-2, 3)]
       print(negdiag, '\n')
       all = (cols, rows, posdiag, negdiag)
       for lst in chain(*all):  # for every list in the chain
           red_counter = 0
           yellow_counter = 0
           for i in lst:
               if i == 'R':
                   yellow_counter = 0
                   red_counter += 1
               if i == 'Y':
                   red_counter = 0
                   yellow_counter += 1
               if red_counter == 4:
                   return 'R'
               if yellow_counter == 4:
                   return 'Y'

if __name__ == '__main__':
   g = Game()
   turn = RED
   while True:
       error = False
       g.print_board()
       row = input('{}\'s turn: '.format('Red' if turn == RED else 'Yellow'))
       try:
           g.insert(int(row), turn)
           turn = YELLOW if turn == RED else RED
           g.get_winner()
       except Exception:
           print("\n DIT KEN NIET\n\n")


