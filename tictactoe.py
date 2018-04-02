empty_squares = [1, 2, 3, 4, 5, 6, 7, 8, 9]
next_turn_is_x = True

if next_turn_is_x == True and len(empty_squares) > 1:
    print("We’ve got empty squares. Player X: ")
elif next_turn_is_x == False and len(empty_squares) > 1:
    print("We’ve got empty squares. Player 0: ")
elif len(empty_squares) == 1:
    print("One last square. This move is given.")
else:
    print("No empty squares. Game over.")
