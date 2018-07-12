from random import randint

class Board:
    def __init__(self):
        board = []
        for i in range(3):
            row = []
            for j in range(3):
                row.append(0)
            board.append(row)
        self.board = board
    
    def copy_board(self, other_board):
        self.board = other_board.board.copy()
    
    def get(self, row, col):
        return self.board[row][col]
    
    def set(self, row, col, player):
        self.board[row][col] = player

    def valid_move(self, row, col):
        if((row >= 0 and row <= 2) and (col >= 0 and col <= 2)):
            if(self.board[row][col] == 0):
                return True
            else:
                return False
        else:
            return False

    def victory(self):
        for i in range(len(self.board)):
            if(self.board[i][0] == self.board[i][1] == self.board[i][2] != 0):
                return self.board[i][1]
        for i in range(len(self.board[i])) :
            if(self.board[0][i] == self.board[1][i] == self.board[2][i] != 0):
                return self.board[1][i]
        if(self.board[0][0] == self.board[1][1] == self.board[2][2] != 0):
            return self.board[1][1]
        if(self.board[0][2] == self.board[1][1] == self.board[2][0] != 0):
            return self.board[1][1]
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if(self.board[i][j] == 0):
                    return 0
        return -1

    def immediate_victory(self, player):
        #0=empty
        #two in a column
        for i in range(0,3):
            empty = False
            score = 0
            for j in range(0,3):
                if self.get(i, j)==0:
                    empty=(i,j)
                elif self.get(i, j)==player:
                    score+=1
            if score==2 and empty!=False:
                return empty

        #two in a row
        for j in range(0,3):
            empty = False
            score = 0
            for i in range(0,3):
                if self.get(i, j)==0:
                    empty=(i,j)
                elif self.get(i, j)==player:
                    score+=1
            if score==2 and empty!=False:
                return empty
        
        #check diagonals
        score =0
        empty = False
        for i in range(0,3):
            if self.get(i, i)==player:
                score+=1
            elif self.get(i, i)==0:
                empty = (i,i)
        if score==2 and empty!=False:
            return empty

        score =0
        empty = False
        for i in range(0,3):
            if self.get(i, 2- i)==player:
                score+=1
            elif self.get(i, 2 - i)==0:
                empty = (i, 2 - i)
        if score==2 and empty!=False:
            return empty

        return False   