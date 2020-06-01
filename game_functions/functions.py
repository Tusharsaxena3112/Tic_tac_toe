# # walk through
# We need to print a board.
# Take in player input.
# Place their input on the board.
# Check if the game is won,tied, lost, or ongoing.
# Repeat c and d until the game has been won or tied.
# Ask if players want to play again.

import random


def player_marker():
    marker = ' '
    while (marker != 'X' or marker != 'O'):
        print("Choose a marker i.e X or O")
        marker = input().upper()
        if (marker == 'X'):
            return ('X', 'O')
        else:
            return ('O', 'X')


def display_board(board):
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-----------')
    print(board[4] + ' | ' + board[4] + ' | ' + board[6])
    print('-----------')
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])


def place_marker(board, position, marker):
    board[position] = marker


# check all rows
# check all the columns
# check all the diagonals

def win_check(board, marker):
    if (board[1] == marker and board[2] == marker and board[3] == marker) or (
            board[4] == marker and board[5] == marker and board[6] == marker) or (
            board[7] == marker and board[8] == marker and board[9] == marker) or (
            board[1] == marker and board[4] == marker and board[7] == marker) or (
            board[2] == marker and board[5] == marker and board[8] == marker) or (
            board[3] == marker and board[6] == marker and board[9] == marker) or (
            board[1] == marker and board[5] == marker and board[9] == marker) or (
            board[3] == marker and board[5] == marker and board[7] == marker):
        return True
    else:
        return False


def who_play_first():
    r = random.randint(0, 1)
    if (r == 0):
        return 'Player 1'
    return 'Player 2'


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1, 10):
        if board[i] == '':
            return False
    return True


def player_posiion():
    position = 0
    while position not in range(1, 10) or not space_check():
        position = int(input('Enter index position :'))

    return position
