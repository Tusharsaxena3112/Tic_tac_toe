from game_functions import functions

# # walk through
# We need to print a board.
# Take in player input.
# Place their input on the board.
# Check if the game is won,tied, lost, or ongoing.
# Repeat c and d until the game has been won or tied.
# Ask if players want to play again.

print('WELCOME TO TIC-TOC-TOE')
while True:

    if not functions.replay():
        break
