from random import randint

class Basic:
    def __init__(self):
        pass
    
    def move(self, board):
        while((not self.valid_move(row, 0) and not self.valid_move(row, 1) and not self.valid_move(row, 2))):
            row = randint(0, 2)
        while(not self.valid_move(row, col)):
            col = randint(0, 2)
        return row, col
    
    def read(self, name):
        pass
    
    def write(self, name):
        pass