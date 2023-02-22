from .base_agent import Agent, Move, valid_moves
from ..player import PLAYER_NAMES, other_player
from ..board import CellState

class SuboptimalAgent (Agent):
    def __init__(self, player):
        super().__init__(player)


        ##new heuristic: tries to complete the game as fast as possible, so it wants the maximizer to win no matter who it is
    def evaluate(self, board, is_maximizer):
        if board.winner is None:
            return 0
        elif (PLAYER_NAMES[board.winner] == PLAYER_NAMES[self._player]):
            return -10
        elif PLAYER_NAMES[board.winner] == PLAYER_NAMES[other_player(self._player)]:
            return 10

    def minimax(self, board, depth, is_maximizer):
        score = self.evaluate(board, is_maximizer)

        # if maximizer or minimzer won
        if score == 10:
            return score
        if score == -10:
            return score
        if depth == 0:
            score = 0
            return score  ##is a tie bc no moves left despite being at a leaf node

        if is_maximizer == True:
            best = -1000  ##should i carry best with me as a param?

            # for move in valid_moves(board, self._player):
            for i in range(board.size):
                for j in range(board.size):
                    if board.cell(i, j) == CellState.EMPTY:
                        # for cell in valid_moves(board, self._player): ##only in empty cells
                        move = Move(self._player, i, j)  ##will be other player in minimizer
                        #               print(board.empty_cells)
                        board.set_cell(move.player, move.row, move.col)
                        #               print(board.empty_cells)

                        # score = self.evaluate(board)
                        best = max(best, self.minimax(board, depth - 1, not is_maximizer))
                        board.set_cell(CellState.EMPTY, move.row, move.col)
                        # board.set_cell(CellState.EMPTY, i, j) ##change the last move's cell back to empty
            return best
        else:
            best = 1000
            # for cell in board.empty_cells:
            # opponent = other_player(self.player)

            # for move in valid_moves(board, CellState.O):
            for i in range(board.size):
                for j in range(board.size):
                    if board.cell(i, j) == CellState.EMPTY:
                        move = Move(other_player(self._player), i, j)
                        board.set_cell(move.player, move.row, move.col)
                        # score = self.evaluate(board)
                        best = min(best, self.minimax(board, depth - 1, not is_maximizer))
                        board.set_cell(CellState.EMPTY, move.row, move.col)

                    # board.set_cell(CellState.EMPTY, i, j)
            return best
    def next_move (self, board):
        best_move = [-1, -1]
        best_score = -100
        try:
            for i in range (board.size):
                for j in range (board.size):
                    if board.cell(i, j) == CellState.EMPTY:
                        move = Move(self._player, i, j)
                        board.set_cell(move.player, move.row, move.col)
                        depth = len(board.empty_cells)
                        score = self.minimax(board, depth, False)
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