empty_squares = [1, 2, 3, 4, 5, 6, 7, 8, 9]
playerX_moves = []
player0_moves = []
next_turn_is_x = True
i = 1

while i < 9:

    if next_turn_is_x == True and len(empty_squares) > 1:
        playermove = int(input("Player X: "))
        empty_squares.remove(playermove)
        playerX_moves.append(playermove)
        print(">>> POSITIONS by X: ", playerX_moves)
        print(">>> POSITIONS by 0: ", player0_moves)
        print(">>> Empty ", empty_squares)
        next_turn_is_x = False
        i += 1
    if next_turn_is_x == False and len(empty_squares) > 1:
        playermove = int(input("Player 0: "))
        empty_squares.remove(playermove)
        player0_moves.append(playermove)
        print(">>> POSITIONS by X: ", playerX_moves)
        print(">>> POSITIONS by 0: ", player0_moves)
        print(">>> Empty ", empty_squares)
        next_turn_is_x = True
        i += 1
    elif len(empty_squares) == 1:
        print("One last square. This move is given.")
    else:
        print("No empty squares. Game over.")
