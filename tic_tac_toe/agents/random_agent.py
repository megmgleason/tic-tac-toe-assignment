import random
import time

from .base_agent import Agent, Move, valid_moves
from ..player import PLAYER_NAMES


class RandomAgent(Agent):
    def __init__(self, player):
        super().__init__(player)

    def next_move(self, board):
        try:
            next_moves = valid_moves(board, self._player)
            print("")
            print("{}'s next move".format(PLAYER_NAMES[self._player]))
            row = -1
            col = -1
            move = Move(self._player, row, col)
            while (move not in next_moves):
                row = random.randint(0,2)
                col = random.randint(0,2)
                move = Move(self._player, row, col)

            print("")

            print("\trow: {}".format(row))
            print("\tcol: {}".format(col))

            return Move(self._player, row, col)
        except ValueError:
            print("Row an col must be integers between 0 and {}".format(
                board.size))


