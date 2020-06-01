# # walk through
# We need to print a board.
# Take in player input.
# Place their input on the board.
# Check if the game is won,tied, lost, or ongoing.
# Repeat c and d until the game has been won or tied.
# Ask if players want to play again.


def player_marker():
    print("Choose a marker i.e X or O")
    marker = input()
    if (marker == 'X'):
        return ('X', 'O')
    else:
        return ('O', 'X')
