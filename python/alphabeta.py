from random import randint
from board import Board

class Alphabeta:
    def __init__(self,player):
        self.player=player
    def alphabeta(self, board, player):

        if board.victory():
            if board.victory() == 3 - player:
              return -1
            elif board.victory() == -1:
              return 0
            elif board.victory() == player:
              return 1

        for i in range(3):
            for j in range(3):
                if board.valid_move(i, j):
                    new_board = Board()
                    new_board.copy_board(board)
                    new_board.set(i,j,player)
                    val = self.alphabeta(new_board, 3 - player)
                      if player == self.player:
                          if val > alpha:
                              alpha = val
                          if alpha >= beta:
                             return beta
                      else:
                          if val < beta:
                              beta = val
                          if beta <= alpha:
                              return alpha
                  if player == self.player:
                      return alpha
                  else:
                     return beta
    def move(self,board):
        a = -2
        choices =[]
        if board == Board():
            return 1,1
        for i in range(3):
            for j in range(3):
                if board.valid_move(i,j):
                    new_board = Board()
                    new_board.copy_board(board)
                    new_board.set(i,j,player)
                    val = self.alphabeta(new_board)
                    if val > a: 
                        a = val
                        choices =[(i,j)]
                    elif val == a:
                        choices.append((i,j))
            return random.choice(choices)

