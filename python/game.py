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
        
    
if __name__ == "__main__":
    running = True
    games = 0
    wins = 0
    losses = 0
    this_game = Game(Board(), Human(), Sarsa(2))
    while(running):
        action = choose_action()
        if(action == "Y"):
            winner = this_game.interactive_game(Human())
            games += 1
            if(winner == 1):
                wins += 1
            elif(winner == 2):
                losses += 1
            print_outcome(winner, "Player1", "Player2")
        if(action == "T"):
            rounds = choose_rounds()
            t_wins, t_losses = this_game.automated_games(rounds, Valid(1))
            end_game("Valid", "Sarsa", rounds, t_wins, t_losses)
        elif(action == "L1"):
            this_game.player1.read("Player1")
        elif(action == "L2"):
            this_game.player2.read("Player2")
        elif(action == "W1"):
            this_game.player1.write("Player1")
        elif(action == "W2"):
            this_game.player2.write("Player2")
        elif(action == "N"):
            running = False
    end_game("Human", "Sarsa", games, wins, losses)
    

