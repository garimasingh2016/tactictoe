from board import Board

def print_board(board):
    out = ""
    for i in range(3):
        for j in range(3):
            if(board.get(i, j) == 1):
                out += 'X'
            elif(board.get(i, j) == 2):
                out += 'O'
            else:
                out += ' '
            if(j != 2):
                out += ' | '
            else:
                out += '\n'
        if(i != 2):
            out += '---------\n'
    print(out)

def make_move(board, player, id):
    print("Player " + str(id) + "'s turn")
    return player.move(board)

def human_move(board):
    row = -1
    col = -1
    while((not board.valid_move(row, 0) and not board.valid_move( row, 1) and not board.valid_move(row, 2))):
        row = input("Choose a row: ")
        try:
            row = int(row)
        except ValueError:
            row = -1
    while(not board.valid_move(row, col)):
        col = input("Choose a column: ")
        try:
            col = int(col)
        except ValueError:
            col = -1
    return row, col

def end_game(id1, id2, total, wins, losses):
    print("Player", str(id1), "played", total, "game(s) with Player", id2, "and won", wins, "time(s), and lost", losses, "time(s)")
    
def choose_action():
    would = ""
    while(would != "Y" and would != "N" and would != "T" and would != "L1" and would != "L2" and would != "W1" and would != "W2"):
        would = input("Choose an action:\n\tY to play the agent\n\tN to end the game\n\tT to train the agent\n\tL to load from an existing file (follow with the player number) \n\tW to write progress to a file (follow with the player number)\n=> ")
        would = would.upper()
    return would

def choose_rounds():
    rounds = -1
    while(rounds <= 0 or rounds > 10000000):
        rounds = input("How many rounds would you like to train? => ")
        try:
            rounds = int(rounds)
        except ValueError:
            rounds = -1
    return rounds

def print_outcome(value, id1, id2):
    if(value == 1):
        print("Player", id1, "wins!")
    elif(value == 2):
        print("Player", id2, "wins!")
    elif(value == -1):
        print("It's a draw!")
    