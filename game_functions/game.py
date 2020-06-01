import random
from os import system, name


def clear():
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')


def player_marker():
    marker = ' '
    while marker != 'X' or marker != 'O':
        print("Choose a marker i.e X or O")
        marker = input().upper()
        if marker == 'X':
            return 'X', 'O'
        else:
            return 'O', 'X'


def display_board(board):
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-----------')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
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
    if r == 0:
        return 'Player 1'
    return 'Player 2'


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1, 10):
        if board[i] == ' ':
            return False
    return True


def player_position():
    position = 0
    while position not in range(1, 10) or not space_check(dis_board, position):
        position = int(input('Enter index position :'))

    return position


def replay():
    choice = input('Do you want play again:(y or n)')
    if choice == 'y':
        return True
    else:
        return False


# # walk through
# We need to print a board.
# Take in player input.
# Place their input on the board.
# Check if the game is won,tied, lost, or ongoing.
# Repeat c and d until the game has been won or tied.
# Ask if players want to play again.

print('WELCOME TO TIC-TOC-TOE')
while True:
    dis_board = [' '] * 10
    player_1, player_2 = player_marker()
    turn = who_play_first()
    print(turn + ' Will go first')
    ready = input('Ready to play (y or n)')
    if ready == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            display_board(dis_board)  # display the board
            dis_position = player_position()  # choosing the player position
            place_marker(dis_board, dis_position, player_1)
            if win_check(dis_board, player_1):
                display_board(dis_board)
                print('PLAYER 1 has won the game!')
                game_on = False
            else:
                if full_board_check(dis_board):
                    display_board(dis_board)
                    print('TIED GAME')
                    game_on = False
                else:
                    turn = 'Player 2'
        else:
            display_board(dis_board)
            dis_position = player_position()  # choosing the player position
            place_marker(dis_board, dis_position, player_2)
            if win_check(dis_board, player_2):
                display_board(dis_board)
                print('PLAYER 2 has won the game!')
                game_on = False
            else:
                if full_board_check(dis_board):
                    display_board(dis_board)
                    print('TIED GAME')
                    game_on = False
                else:
                    turn = 'Player 1'

    if not replay():
        break
