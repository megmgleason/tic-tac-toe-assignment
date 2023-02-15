from .base_agent import Agent, Move, valid_moves
from ..player import PLAYER_NAMES, other_player, Player
from tic_tac_toe.board import Board, CellState
import math
import random





class SmartAgentPruning(Agent):
    def __init__(self, player):
        super().__init__(player)

    def evaluate(self, board):

        if board.winner is None:
            return 0
        elif PLAYER_NAMES[board.winner] == PLAYER_NAMES[self._player]:  # THIS WAS WHAT WAS WRONG ~ i needed to check if the PLAYER_NAMES was both the winner and the appropriate player
            return 10
        elif PLAYER_NAMES[board.winner] == PLAYER_NAMES[other_player(self._player)]:
            return -10

        ##minimax
        ##It considers all possible ways the board can go and return the optimal value of the board
        ##params:
        ##self - instance of smart_agent
        ##board - current setup of the board
        # depth - depth of the tree (why is this necessary?)
        # is_maximizer: True if the current player is the maximizer (X). Will switch throughout program to mimic taking turns

    def minimax(self, board, depth, alpha, beta, is_maximizer):
        score = self.evaluate(board)

        # if maximizer or minimzer won
        if score == 10:
            return score
        if score == -10:
            return score
        if depth == 0:
            score = 0
            return score  ##is a tie bc no moves left despite being at a leaf node

        if is_maximizer:
            max_eval = -1000
            for i in range(board.size):
                for j in range(board.size):
                    if board.cell(i, j) == CellState.EMPTY:
                        move = Move(self._player, i, j)
                        board.set_cell(move.player, move.row, move.col)
                        eval = self.minimax(board, depth - 1, alpha, beta, not is_maximizer)
                        #best = max(best, self.minimax(board, depth - 1, alpha, beta, not is_maximizer))
                        max_eval = max(max_eval, eval)
                        alpha = max (alpha, eval)
                        if beta <= alpha:
                            break
                        board.set_cell(CellState.EMPTY, move.row, move.col)
            return max_eval
        else:
            min_eval = 1000
            for i in range(board.size):
                for j in range(board.size):
                    if board.cell(i, j) == CellState.EMPTY:
                        move = Move(other_player(self._player), i, j)
                        board.set_cell(move.player, move.row, move.col)
                        eval = self.minimax(board, depth - 1, alpha, beta, not is_maximizer)
                        #best = min(best, self.minimax(board, depth - 1, alpha, beta, not is_maximizer))
                        min_eval = min(min_eval, eval)
                        beta = min(beta, eval)
                        if beta <= alpha:
                            break
                        board.set_cell(CellState.EMPTY, move.row, move.col)
            return min_eval



    def next_move(self, board):
        best_move = [-1, -1]
        best_score = -100
        alpha = -10000
        beta = 10000
        try:
            if len(board.empty_cells) == 9:
                best_move[0] = random.randint(0, 2)
                best_move[1] = random.randint(0, 2)
                move = Move(self._player, best_move[0], best_move[1])
            else:
                for i in range(board.size):
                    for j in range(board.size):
                        if board.cell(i, j) == CellState.EMPTY:

                            move = Move(self._player, i, j)
                            board.set_cell(move.player, move.row, move.col)
                            depth = len(board.empty_cells)
                            score = self.minimax(board, depth, alpha, beta, False)
                            board.set_cell(CellState.EMPTY, move.row, move.col)

                            if score > best_score:
                                best_score = score
                                best_move[0] = i
                                best_move[1] = j

            print("")
            print("{}'s next move".format(PLAYER_NAMES[self._player]))
            print("\trow: {}".format(best_move[0]))
            print("\tcol: {}".format(best_move[1]))
            print("")
            return Move(self._player, best_move[0], best_move[1])

        except ValueError:
            print("Row an col must be integers between 0 and {}".format(board.size))
