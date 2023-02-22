from .base_agent import Agent, Move, valid_moves
from ..player import PLAYER_NAMES, other_player
from tic_tac_toe.board import Board, CellState
import math
import random


##I need to rethink how I'm traversing it, because in my head I keep visualizing a tree but I step through the empty cells array one element at a time,
##need to examine each cell's value, then it's "children" as if it were a tree. Different than +1

##new minimax: pass in the board using the variable that has the states and blank cells.
##iterate through that variable using a for loop 0-2, do AB checks

#make the array of empty cells into a tree. every time the minimax pruning algo is called (once per turn), the tree will likely need refactoring bc of pruning.




class SmartAgentPruning(Agent):
    def __init__(self, player):
        super().__init__(player)

    #change the way you evaluate. If depth == size, then check to see if win, loss or tie and return that number
    def evaluate(self, board):
        if (board.winner is None):
            if len(board.empty_cells) == 0:##this is a tie
                return 0 ##tie, stop the game
        elif PLAYER_NAMES[board.winner] == PLAYER_NAMES[self._player]:  # THIS WAS WHAT WAS WRONG ~ i needed to check if the PLAYER_NAMES was both the winner and the appropriate player
            return 10
        elif PLAYER_NAMES[board.winner] == PLAYER_NAMES[other_player(self._player)]:
            return -10
        else:
            return None ##no winner but not a tie, meaning there are open spaces, continue the game

        ##minimax
        ##It considers all possible ways the board can go and return the optimal value of the board
        ##params:
        ##self - instance of smart_agent
        ##board - current setup of the board
        # depth - depth of the tree (why is this necessary?)
        # is_maximizer: True if the current player is the maximizer (X). Will switch throughout program to mimic taking turns

    def minimax(self, board, tree, depth, node_index, alpha, beta, is_maximizer):
        #score = self.evaluate(board)

        #new base case: leaf node reached, return that evaluation value
        # if depth == 4:
        #     score = self.evaluate(board)
        #     return score

        # if maximizer or minimzer won
        # if score == 10:
        #     return score
        # if score == -10:
        #     return score
        # if depth == 0:
        #     score = 0
        #     return score  ##is a tie bc no moves left despite being at a leaf node

        #first time thru index is at 1, pointing to (0,0)
        if is_maximizer:

            max_eval = -1000
            px = None
            py = None
            result = self.evaluate(board)

            if result == 10:
                return (1,0,0)
            elif result == -10:
                return (-1,0,0)
            elif result == 0:
                return (0,0,0)
            # for i in range (0,2):
                # move = tree[i]
               # eval = minimax()
               #  space = tree[node_index]
               #  move = Move(self._player, space[0], space[1])
               #  board.set_cell(move.player, move.row, move.col)
               #  eval = self.minimax(board, tree, depth + 1, node_index * 2 + i, alpha, beta, not is_maximizer)
               #  max_eval = max(max_eval, eval)
               #  alpha = max(alpha, max_eval)
            for i in range (board.size):
                for j in range(board.size):
                    if board.cell(i,j) == CellState.EMPTY:
                        move = Move(self._player,i,j)
                        board.set_cell(move.player, move.row, move.col)
                        (m, min_i, in_j) = self.minimax(board, tree, depth, node_index, alpha, beta, not is_maximizer)
                        if m > max_eval:
                            max_eval = m
                            px = i
                            py = j
                        board.set_cell(CellState.EMPTY, i, j)
                        if max_eval >= beta:
                            return(max_eval,px, py)
                        if max_eval > alpha:
                            alpha = max_eval
            return (max_eval, px, py)


            # for i in range(board.size):
            #     for j in range(board.size):
            #         if board.cell(i, j) == CellState.EMPTY:
            #             move = Move(self._player, i, j)
            #             board.set_cell(move.player, move.row, move.col)
            #             eval = self.minimax(board, depth - 1, alpha, beta, not is_maximizer)
            #             #best = max(best, self.minimax(board, depth - 1, alpha, beta, not is_maximizer))
            #             max_eval = max(max_eval, eval)
            #             alpha = max (alpha, max_eval) #not just eval!
            #             if beta <= alpha:
            #                 break
            #             #board.set_cell(CellState.EMPTY, move.row, move.col)
            # return max_eval
        else:
            min_eval = 1000
            qx = None
            qy = None
            result = self.evaluate(board)

            if result == 10:
                return (1,0,0)
            elif result == -10:
                return (-1, 0, 0)
            elif result == 0:
                return (0,0,0)

            for i in range(board.size):
                for j in range(board.size):
                    if board.cell(i,j) == CellState.EMPTY:
                        move = Move(other_player(self._player), i, j)
                        board.set_cell(move.player, move.row, move.col)
                        (m, max_i, max_j) = self.minimax(board,tree,depth, node_index, alpha, beta, not is_maximizer)
                        if m < min_eval:
                            min_eval = m
                            qx = i
                            qy = j
                        board.set_cell(CellState.EMPTY, i, j)
                        ##continue w site! then test code
                        if min_eval <= alpha:
                            return (min_eval,qx, qy)
                        if min_eval < beta:
                            beta = min_eval

            return (min_eval, qx, qy)


            # for i in range (0,2):
            #     space = tree[node_index]
            #     move = Move(other_player(self._player), space[0], space[1] )
            #     board.set_cell(move.player, move.row, move.col)
            #     eval = self.minimax(board, tree, depth + 1, node_index * 2 + i, alpha, beta, not is_maximizer)
            #     min_eval = min(min_eval, eval)
            #     beta =  min(beta, min_eval)
            #     if beta <= alpha:
            #         break
            # for i in range(board.size):
            #     for j in range(board.size):
            #         if board.cell(i, j) == CellState.EMPTY:
            #             move = Move(other_player(self._player), i, j)
            #             board.set_cell(move.player, move.row, move.col)
            #             eval = self.minimax(board, depth - 1, alpha, beta, not is_maximizer)
            #             #best = min(best, self.minimax(board, depth - 1, alpha, beta, not is_maximizer))
            #             min_eval = min(min_eval, eval)
            #             beta = min(beta, min_eval) #not just eval!
            #             if beta <= alpha:
            #                 break
            #             #board.set_cell(CellState.EMPTY, move.row, move.col)
            # return min_eval



    def next_move(self, board):
        best_move = [-1, -1]
        best_score = -100
        alpha = -10000
        beta = 10000
        elm_index = 0
        depth = board.size

        tree = [(-5, 0)]
        for c in board.empty_cells:
            tree.append(c)

        try:
            (v, row, col) = self.minimax(board, tree, 0, 1, alpha, beta, True)
            move = (row, col)


            # if len(board.empty_cells) == 9:
            #     best_move[0] = random.randint(0, 2)
            #     best_move[1] = random.randint(0, 2)
            #     move = Move(self._player, best_move[0], best_move[1])
            # else:
            # for i in range(board.size):
            #     for j in range(board.size):
            #         if board.cell(i, j) == CellState.EMPTY:
            #
            #             move = Move(self._player, i, j)
            #             board.set_cell(move.player, move.row, move.col)
            #             depth = 1
            #             score = self.minimax(board, depth, 0, alpha, beta, False)
            #             board.set_cell(CellState.EMPTY, move.row, move.col)
            #
            #             if score > best_score:
            #                 best_score = score
            #                 best_move[0] = i
            #                 best_move[1] = j



            print("")
            print("{}'s next move".format(PLAYER_NAMES[self._player]))
            print("\trow: {}".format(move[0]))
            print("\tcol: {}".format(move[1]))
            print("")
            return Move(self._player, move[0], move[1])

        except ValueError:
            print("Row an col must be integers between 0 and {}".format(board.size))
