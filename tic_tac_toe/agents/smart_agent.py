from .base_agent import Agent, Move, valid_moves
from ..player import PLAYER_NAMES, other_player, Player
from tic_tac_toe.board import Board, CellState
from copy import copy


class SmartAgent(Agent):
    def __init__(self, player):
        super().__init__(player)
        #self.isMaximizingPlayer = True
        # if PLAYER_NAMES[self._player] == 'x':
        #     self.isMaximizingPlayer = True
        #
        # else:
        #     self.isMaximizingPlayer = False

        ##what if i started by assuming all the smart agents were the maximizing players? not just O?

    ##will take in a board, according to if current player has won +10, if other player has won -10, neither is 0, meaning it needs to traverse more nodes.
    def evaluate(self, board):
        #print("board winner {}:".format(board.winner))
        if board.winner is None:
            #print("none!")
            return 0

        elif PLAYER_NAMES[board.winner] == PLAYER_NAMES[self._player]: #THIS WAS WHAT WAS WRONG ~ i needed to check if the PLAYER_NAMES was both the winner and the appropriate player
            #print("x won")
            return 10

        elif PLAYER_NAMES[board.winner] == PLAYER_NAMES[other_player(self._player)]:
            return -10
        ##this method should be fine now, go and adjust minimax to what I wrote on GFG IDE




    ##minimax
    ##It considers all possible ways the board can go and return the optimal value of the board
    ##params:
    ##self - instance of smart_agent
    ##board - current setup of the board
    # depth - depth of the tree (why is this necessary?)
    #is_maximizer: True if the current player is the maximizer (X). Will switch throughout program to mimic taking turns
    def minimax(self, board, depth, is_maximizer):
        score = self.evaluate(board)

        # if maximizer or minimzer won
        if score == 10:
            return score
        if score == -10:
            return score
        if depth == 0:
            score = 0
            return score  ##is a tie bc no moves left despite being at a leaf node

        if is_maximizer == True:
            best = -1000##should i carry best with me as a param?

            #for move in valid_moves(board, self._player):
            for i in range (board.size):
                for j in range(board.size):
                    if board.cell(i,j) == CellState.EMPTY:
            #for cell in valid_moves(board, self._player): ##only in empty cells
                        move = Move(self._player, i, j)  ##will be other player in minimizer
 #               print(board.empty_cells)
                        board.set_cell(move.player, move.row, move.col)
 #               print(board.empty_cells)

                # score = self.evaluate(board)
                        best = max(best, self.minimax(board, depth - 1, not is_maximizer))
                        board.set_cell(CellState.EMPTY, move.row, move.col)
                        #board.set_cell(CellState.EMPTY, i, j) ##change the last move's cell back to empty
            return best
        else:
            best = 1000
            #for cell in board.empty_cells:
            #opponent = other_player(self.player)

            #for move in valid_moves(board, CellState.O):
            for i in range (board.size):
                for j in range (board.size):
                    if board.cell(i,j) == CellState.EMPTY:
                        move = Move(other_player(self._player), i, j)
                        board.set_cell(move.player, move.row, move.col)
                # score = self.evaluate(board)
                        best = min(best, self.minimax(board, depth - 1, not is_maximizer))
                        board.set_cell(CellState.EMPTY, move.row, move.col)



                    #board.set_cell(CellState.EMPTY, i, j)
            return best


    def minimax_alt (self, board, cur_player, is_maximizer):
        if board.winner is None:
            if len(board.empty_cells) == 0:
                return 0
        elif PLAYER_NAMES[board.winner] == cur_player:
            return 10
        elif PLAYER_NAMES[board.winner] == 'x' or PLAYER_NAMES[board.winner] == 'o':
            return -10

        #cur_player = 'o' if other_player(self._player) is Player.X else 'x'
        scores = []
        for move in valid_moves(board, cur_player):
            move = Move(cur_player, move[0], move[1])
            board.set_cell(cur_player, move[0], move[1])
            scores.append(self.minimax_alt(board, other_player(cur_player), not is_maximizer))
        return max(scores) if is_maximizer else min(scores)





    ##returns the best move to maximize gameplay
    def next_move(self, board):

        best_move = [-1, -1]
        best_score = -100
        # num_repeats = len(board.empty_cells)
        # empty_cells = board.empty_cells
        try:
            #should i clear the move it made before the end of each iteration?
            # while num_repeats > 0:
            #     move_val = self.minimax(board, len(board.empty_cells), self.isMaximizingPlayer)
            #     print("move val: {}".format(move_val))
            #     print("new best score: {}".format(best_score))
            #
            #
            #     num_repeats = num_repeats - 1

            ##do number of repeats based on length, and track the empty cells
            ##each repeat you make the move in that corresponding empty cell and calculate the value, setting it back to
            ##empty each time while still stepping thru the empty_cell array (is a list of tuples, is x,y

            for i in range (board.size):
                for j in range (board.size):
                    if board.cell(i, j) == CellState.EMPTY:
            # for i in range (0, num_repeats):

                ##alternative, what if i adjusted minimax to take in param so it evaluates the board FOR PUTTING X OR O ONLY IN THIS POSITION
                ##make the move here, then call minimax on that!

                        move = Move(self._player, i, j)
                        board.set_cell(move.player, move.row, move.col)
                        depth = len(board.empty_cells)
                        score = self.minimax(board, depth, False)
                        board.set_cell(CellState.EMPTY, move.row, move.col)
                    #current_move = [empty_cells[i][0], empty_cells[i][1]]
                    #board.set_cell(self._player, current_move[0], current_move[1])
                    #move_val = self.minimax(board, len(board.empty_cells), not self.isMaximizingPlayer)
                    #board.set_cell(CellState.EMPTY, move[0], move[1])
                        if score > best_score:
                            best_score = score
                            best_move[0] = i
                            best_move[1] = j
                        #board.set_cell(self._player, current_move[0], current_move[1])
                        # print("new best score: {}".format(best_score))
                        # print("new best move: {}".format(best_move))

            print("")
            print("{}'s next move".format(PLAYER_NAMES[self._player]))
            print("\trow: {}".format(best_move[0]))
            print("\tcol: {}".format(best_move[1]))
            print("")

            return Move(self._player, best_move[0], best_move[1])

            #board.set_cell(CellState.EMPTY, row, col)
                #print("now will clear the board at that place")
                #this might cause the x to be placed in the same spot...
                #board.set_cell(CellState.EMPTY, empty_cell[0], empty_cell[1])

            # for i in range (0, 9):
        #for cell in board_copy.empty_cells:
         #   Move(self._player, cell[0], cell[1])
        # for row in board.rows:
        #     for col in board.cols:
        #         if row[col] in board.empty_cells:
        #             move_val = self.minimax(board, 9, self.isMaximizingPlayer)
        #             current_move = (row, col)
        #             print("minimax's score :{}".format(move_val))
        #         #current_move = valid_moves(board_copy, self._player).pop(0)
        #     # board.set_cell(CellState.EMPTY, cell[0], cell[1])
        #             if move_val > best_score:
        #                 best_score = move_val
        #                 best_move = current_move
        #print("the best score for row : {}".format(row, best_score))

        # return move_val
        #return Move(self._player, best_move[0], best_move[1])


        # print("is there a winner? {}".format(board.winner))
        # if board_copy.winner == None:
        #     print("should print none!")
        # print(self.isMaximizingPlayer)
        ##this needs to return the cell that is the best move

        ##bc of the abstract method, if we do not return a Move() we will get an assertion error
        ##have minimax return the best possible value and move,
        ##check to see if the calling object is a maximzer or a minimizer.(?)


        except ValueError:
            print("Row an col must be integers between 0 and {}".format(board.size))
