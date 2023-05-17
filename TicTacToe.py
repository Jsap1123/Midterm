import random

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R']);
    print('-+-+-');
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R']);
    print('-+-+-');
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R']);


def isWinner(board, letter):
    return ((board['top-L'] == letter and board['top-M'] == letter and board['top-R'] == letter) or # across the top
     (board['mid-L'] == letter and board['mid-M'] == letter and board['mid-R'] == letter) or # across the middle
     (board['low-L'] == letter and board['low-M'] == letter and board['low-R'] == letter) or # across the bottom
     (board['top-L'] == letter and board['mid-L'] == letter and board['low-L'] == letter) or # down the left side
     (board['top-M'] == letter and board['mid-M'] == letter and board['low-M'] == letter) or # down the middle
     (board['top-R'] == letter and board['mid-R'] == letter and board['low-R'] == letter) or # down the right side
     (board['top-L'] == letter and board['mid-M'] == letter and board['low-R'] == letter) or # diagonal
     (board['top-R'] == letter and board['mid-M'] == letter and board['low-L'] == letter)) # diagonal


playAgain = 'yes'

while playAgain == 'yes':

    print('Welcome to Tic-Tac-Toe.')
    theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
                'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
                'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
    print('Would you like to play 1 or 2 player?')
    numPlayers = input()
    turn = 'X'
    for i in range(9):
        printBoard(theBoard)
        if numPlayers == '1' and turn == 'O':
            print('Computers turn.')
            move = random.choice(list(theBoard.keys()))
            while theBoard[move] != ' ':
                move = random.choice(list(theBoard.keys()))
        else:
            print('Turn for ' + turn + '. Move on which space?')
            move = input()
            while move not in theBoard or theBoard[move] != ' ':
                print('invalid move. pick another')
                move = input()
        theBoard[move] = turn
        if isWinner(theBoard, turn):
            print(turn + ' has won the game.')
            printBoard(theBoard)
            break

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    print('Would you like to play again, yes or no?')
    playAgain = input()
    print()




