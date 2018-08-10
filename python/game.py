from board import Board
from human import Human
from basic import Basic
from valid import Valid
from sarsa import Sarsa
from text_view_utils import print_board, make_move, end_game, choose_action, choose_rounds, print_outcome

class Game:
    
    def __init__(self, board, player1, player2):
        self.board = board
        self.player1 = player1
        self.player2 = player2
    
    def interactive_game(self, player1 = None, player2 = None):
        if(player1 != None):
            self.player1 = player1
        if(player2 != None):
            self.player2 = player2
        x = True
        self.board = Board()
        while(not self.board.victory()):
            print_board(self.board)
            if(x):
                row, col= make_move(self.board, self.player1, 1)
                self.board.set(row, col, 1)
            else:
                row, col = make_move(self.board, self.player2, 2)
                self.board.set(row, col, 2)
            x = not x
        print_board(self.board)
        return self.board.victory()

    def automated_games(self, rounds, player1 = None, player2 = None):
        if(player1 != None):
            self.player1 = player1
        if(player2 != None):
            self.player2 = player2
        agent_wins = 0
        agent_losses = 0
        y = True
        for i in range(rounds):
            board = Board()
            while(not board.victory()):
                if(y):
                    row, col = self.player1.move(board)
                    board.set(row, col, 1)
                else:
                    row, col = self.player2.move(board)
                    board.set(row, col, 2)
                y = not y
            if(board.victory() == 1):
                agent_wins += 1
            if(board.victory() == 2):
                agent_losses += 1
        return agent_wins, agent_losses