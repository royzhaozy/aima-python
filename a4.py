"""
Assignment 4 for CMPT 310
Summer 2019, Simon Fraser University
Ziyi Zhao, 301244109
"""

from random import choice
from copy import deepcopy

human = 0
computer = 1


def display(board):
    print('-------------')
    for i in range (3):
        print ('|', end=' ')
        for j in range (3):
            if board [3 * i + j] == 0:
                print ('O', end=' | ')
            elif board [3 * i + j] == 1:
                print ('X', end=' | ')
            else:
                print (' ', end=' | ')
        print('\n-------------')

def emptySquare(board):
    return [i for i, x in enumerate (board) if x == None]

def move(board, player, x):
    if x < 9 and board [x] == None:
        board [x] = player
    else:
        print("Illegal Move, please try again")
    return board

def gameOver(board):
    winning_conditions = 8
    for i in range(0, 3):
        colon = [board[i], board[i + 3], board[i + 6]]
        if human in colon:
            if computer in colon:
                winning_conditions -= 1
            elif None not in colon:
                return True, -5 # Computer lost
        elif None not in colon:
            return True, 1 # Computer won

    for i in range(0, 9, 3):
        row = [board[i], board[i + 1], board[i + 2]]
        if human in row:
            if computer in row:
                winning_conditions -= 1
            elif None not in row:
                return True, -5 # Computer lost
        elif None not in row:
            return True, 1 # Computer won

    for i in [2,4]:
        diag = [board[4 - i], board[4], board[4 + i]]
        if human in diag:
            if computer in diag:
                winning_conditions -= 1
            elif None not in diag:
                return True, -5 # Computer lost
        elif None not in diag:
            return True, 1 # Computer won

    if winning_conditions == 0:
        return True, 0

    return False, None

def random_playout(board, nextPlayer):
    result = gameOver(board)
    if result[0]:
        return result[1]
    board = move(board, nextPlayer, choice(emptySquare(board)))
    return random_playout(board, not nextPlayer)

def play_a_new_game(difficulty = 20, board = [None]*9):
    print("This is a game of tic tac toe, the board is laid out below")
    print("-------------\n"
          "| 0 | 1 | 2 |\n"
          "-------------\n"
          "| 3 | 4 | 5 |\n"
          "-------------\n"
          "| 6 | 7 | 8 |\n"
          "-------------")
    player = int(input("Who do you want to starts first (0 for human, 1 for computer): ")) % 2
    while True:
        if player == human:
            x = int(input("Please enter the next move: "))
            if x not in emptySquare(board):
                print("Space taken, please try again")
                continue
            board = move(board, player, x)
        else:
            print("Computer's move:")
            legalMoves = emptySquare(board)
            score = [0] * len(legalMoves)
            for i in range(len(score)):
                for j in range(difficulty):
                    simBoard = deepcopy(board)
                    simBoard[legalMoves[i]] = computer
                    result = random_playout(simBoard, human)
                    score[i] += result
            board = move(board, player, legalMoves[score.index(max(score))])
        display(board)
        result = gameOver(board)
        if result[0]:
            if result[1] == 0:
                print("The game has tied")
            elif result[1] == 1:
                print("Computer has won the game")
            else:
                print("Human has won the game")
            return
        player = not player


if __name__ == '__main__':
    board = [None ,0,None, None, 1, None, 0, 1, None]
    play_a_new_game(20, board)
    # play_a_new_game()