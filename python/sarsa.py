from random import randint, random
import json
from board import Board

class Sarsa:
    
    def __init__(self, player, alpha = .4 , gamma = .4, epsilon = .05, table = None):
        if(table == None):  
            table = []
            for i in range(3 ** 9):
                state = []
                for j in range(9):
                    state.append(0)
                table.append(state)
        self.table = table
        self.player = player
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon

    def calculate_state(self, board):
        state = 0
        for i in range(3):
            for j in range(3):
                state += board.get(i, j) * (3 ** (i * 3 + j))
        return state
                    
    def q_select(self, board):
        e = random()
        state = self.calculate_state(board)
        row = -1
        col = -1
        if(e > self.epsilon):
            a = self.table[state].index(max(self.table[state]))
            row = a // 3
            col = a % 3
        while(not board.valid_move(row, col)):
            a = randint(0, 8)
            row = a // 3
            col = a % 3
        return a
    
    def reward(self, board):
        out = 0
        if(board.victory() == self.player):
            out += 100
        if(board.victory() == 3 - self.player):
            out += -100
        if(board.victory() == -1):
            out += -50
        if(board.immediate_victory(self.player) != False):
            out += 25
        if(board.immediate_victory(3 - self.player) != False):
            out += -100
        return out

    def move(self, board):
        a = self.q_select(board)
        state = self.calculate_state(board)
        row = a // 3
        col = a % 3
        stateprime = state + self.player * (3 ** (a))
        boardprime = Board()
        boardprime.copy_board(board)
        boardprime.set(row, col, self.player)
        if(boardprime.victory() == 0):
            aprime = self.q_select(boardprime)
            self.table[state][a] = self.table[state][a]  + self.alpha * (self.reward(boardprime) + self.gamma * (self.table[stateprime][aprime]) - self.table[state][a])
        else:
            self.table[state][a] = self.table[state][a]  + self.alpha * (self.reward(boardprime) - self.table[state][a])
        return row, col

    def read(self, name):
        with open(name + '.json') as json_file:
            agent_data = json.load(json_file)
        json_file.close()
        if('player' in agent_data.keys() and 'alpha' in agent_data.keys() and 'gamma' in agent_data.keys() and 'epsilon' in agent_data.keys() and 'table' in agent_data.keys()):
            return Sarsa(agent_data['player'], agent_data['alpha'], agent_data['gamma'], agent_data['epsilon'])
    
    def write(self, name):
        agent_data = {}
        agent_data['name'] = name
        agent_data['player'] = self.player
        agent_data['alpha'] = self.alpha
        agent_data['gamma'] = self.gamma
        agent_data['epsilon'] = self.epsilon
        agent_data['table'] = self.table
        with open(name + '.json', 'w+') as outfile:
            json.dump(agent_data, outfile)
        outfile.close()
