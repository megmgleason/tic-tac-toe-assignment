from .base_agent import Agent, Move, valid_moves
from ..player import PLAYER_NAMES, other_player
from ..board import CellState

class SuboptimalAgent (Agent):
    def __init__(self, player):
        super().__init__(player)


        ##new heuristic: tries to complete the game as fast as possible, so it wants the maximizer to win no matter who it is
    def evaluate(self, board, is_maximizer):
        if (board.winner is None):
            if len(board.empty_cells) == 0:  ##this is a tie
                return 0  ##tie, stop the game
        elif PLAYER_NAMES[board.winner] == PLAYER_NAMES[self._player]:  # THIS WAS WHAT WAS WRONG ~ i needed to check if the PLAYER_NAMES was both the winner and the appropriate player
            return -10
        elif PLAYER_NAMES[board.winner] == PLAYER_NAMES[other_player(self._player)]:
            return 10
        else:
            return None  ##no winner but not a tie, meaning there are open spaces, continue the game

    def minimax(self, board, tree, depth, node_index, alpha, beta, is_maximizer):
        score = self.evaluate(board, is_maximizer)

        # if maximizer or minimzer won

        if is_maximizer == True:
            max_eval = -1000
            px = None
            py = None
            result = self.evaluate(board, is_maximizer)

            if result == 10:
                return (1,0,0)
            elif result == -10:
                return (-1,0,0)
            elif result == 0:
                return (0,0,0)

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

        else:
            min_eval = 1000
            qx = None
            qy = None
            result = self.evaluate(board, is_maximizer)

            if result == 10:
                return (1, 0, 0)
            elif result == -10:
                return (-1, 0, 0)
            elif result == 0:
                return (0, 0, 0)

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
    def next_move (self, board):
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
            print("")
            print("{}'s next move".format(PLAYER_NAMES[self._player]))
            print("\trow: {}".format(move[0]))
            print("\tcol: {}".format(move[1]))
            print("")
            return Move(self._player, move[0], move[1])


        except ValueError:
            print("Row an col must be integers between 0 and {}".format(board.size))