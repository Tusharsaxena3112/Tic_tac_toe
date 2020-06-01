# # walk through
# We need to print a board.
# Take in player input.
# Place their input on the board.
# Check if the game is won,tied, lost, or ongoing.
# Repeat c and d until the game has been won or tied.
# Ask if players want to play again.


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
