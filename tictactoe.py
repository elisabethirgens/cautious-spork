empty_squares = [1, 2, 3, 4, 5, 6, 7, 8, 9]

if len(empty_squares) > 1:
    print("We’ve got empty squares. Let’s play!")
elif len(empty_squares) == 1:
    print("One last square. This move is given.")
else:
    print("No empty squares. Game over.")
