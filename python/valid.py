from random import randint
from board import Board

class Valid:
    
    def __init__(self, player):
        self.player = player

    def move(self, board):
        #recives 3x3 matrix of board state
        #return tuple of next move
        move = board.immediate_victory(self.player)
        if (move!=False):
                return move
        else:
            row = -1
            col = -1
            while((not board.valid_move(row, 0) and not board.valid_move(row, 1) and not board.valid_move(row, 2))):
                row = randint(0, 2)
            while(not board.valid_move(row, col)):
                col = randint(0, 2)
            return row, col
    def read(self, name):
        pass
    
    def write(self, name):
        pass