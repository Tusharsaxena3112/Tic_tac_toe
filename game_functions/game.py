from game_functions import functions as f

# # walk through
# We need to print a board.
# Take in player input.
# Place their input on the board.
# Check if the game is won,tied, lost, or ongoing.
# Repeat c and d until the game has been won or tied.
# Ask if players want to play again.

print('WELCOME TO TIC-TOC-TOE')
while True:
    board = [' '] * 10
    player_1, player_2 = f.player_marker()
    turn = f.who_play_first()
    ready = input('Ready to play (y or n)')
    if ready == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            f.display_board(board)  # display the board
            position = f.player_position()  # choosing the player position
            f.place_marker(board, position, player_1)
            if f.win_check(board, player_1):
                f.display_board(board)
                print('PLAYER 1 has won the game!')
                game_on = False
            else:
                if f.full_board_check(board):
                    f.display_board(board)
                    print('TIED GAME')
                    game_on = False
                else:
                    turn = 'Player 2'
        else:
            f.display_board(board)
            position = f.player_position()  # choosing the player position
            f.place_marker(board, position, player_2)
            if f.win_check(board, player_2):
                f.display_board(board)
                print('PLAYER 2 has won the game!')
                game_on = False
            else:
                if f.full_board_check(board):
                    f.display_board(board)
                    print('TIED GAME')
                    game_on = False
                else:
                    turn = 'Player 1'

    if not f.replay():
        break
