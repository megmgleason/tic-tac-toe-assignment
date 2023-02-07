from pprint import pprint

from .base_agent import Agent, Move, valid_moves
from ..player import PLAYER_NAMES


class ConsoleInputAgent(Agent):
    def __init__(self, player):
        super().__init__(player)

    def evaluate(self, board):
        ##using winner property of board to return a line winner, if it is X +10, if it is 0, -10

        if board.winner == 'x':
            print("winner was detected")
            print("evaluate found x winning, return 10")
            return 10
        elif board.winner == PLAYER_NAMES[self._player] == 'o':
            print("evaluate found o winning, return -10")
            return -10

        print("evaluate didnt find a winner, return 0")
        return 0

    def next_move(self, board):
        def _input_move():
            try:
                print("")
                print("{}'s next move".format(PLAYER_NAMES[self._player]))
                row = int(input("\trow: "))
                col = int(input("\tcol: "))
                print("")
                return Move(self._player, row, col)
            except ValueError:
                print("Row an col must be integers between 0 and {}".format(
                    board.size))

        move = _input_move()
        next_moves = valid_moves(board, self._player)

        while move not in next_moves:
            print("{} is not valid, try again.".format(move))
            print("Valid moves: ")
            pprint(next_moves)
            move = _input_move()

        return move


