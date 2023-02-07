import random
import math

from .base_agent import Agent, Move, valid_moves
from ..player import PLAYER_NAMES, Player


def evaluate (board):
    ##using winner property of board to return a line winner, if it is X +10, if it is 0, -10
    board.set_cell('x', 0, 0)
    board.set_cell('x', 0, 1)
    board.set_cell('x', 0, 2)


    if board.winner[0] == Player.ALL_PLAYERS[0]:
        print("winner was detected")
        print("evaluate found x winning, return 10")
        return 10
    elif board.winner[0] == Player.ALL_PLAYERS[1]:
        print("evaluate found o winning, return -10")
        return -10

    print("evaluate didnt find a winner, return 0")
    return 0

class RandomAgent(Agent):
    def __init__(self, player):
        super().__init__(player)
        if PLAYER_NAMES[self._player] == 'x':
            self.isMaximizingPlayer = True
            print("X is maximizing player")
        else:
            self.isMaximizingPlayer = False
            print("O is minimizing player")

    def next_move(self, board):
        try:
                ##do I make a new DFS minimax agent or do i change the implementaiton of this?
                ##I could hard code it in, first just change next_move to be DFS minimax, then for 1 random 1 DFS, could
                ##do logic to see that if the character is X that one is minimax eg.

                ##random move
            next_moves = valid_moves(board, self._player)
            print("")
            print("{}'s next move".format(PLAYER_NAMES[self._player]))
            row = -1
            col = -1
            move = Move(self._player, row, col)
            while (move not in next_moves):
                row = random.randint(0, 2)
                col = random.randint(0, 2)
                move = Move(self._player, row, col)

            print("")

            print("\trow: {}".format(row))
            print("\tcol: {}".format(col))
            print("")
           # eval = evaluate(board)

            return Move(self._player, row, col)
        except ValueError:
            print("Row an col must be integers between 0 and {}".format(board.size))




    ##finds and returns the best row and column to maximize the X utility, done by doing a DFS
    ##What I need: the board (to track the state), pass in self._player so we know whose turn it is
    def minimax(self, board, current_player):

        row = 0
        col = 0 #just for illistration purposes
        if PLAYER_NAMES[self._player] == 'x':
            print("x's turn, maximize")
            # other_player = 'O'
            maxEval = -math.inf
        else:
            print("o's turn, minimize")
            # other_player = 'X'
            minEval = math.inf

        ##return Move(self._player, row, col) that minimax returns

        return Move(self._player, row, col)

