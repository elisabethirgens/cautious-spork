empty_squares = [1, 2, 3, 4, 5, 6, 7, 8, 9]
playerX_moves = []
player0_moves = []

print("""
Let’s play tic-tac-toe! The developer is a newbie python coder 🐍
so for now, plz only type integers from the empty list. 😜
""")

def game():

    if len(empty_squares) > 1:

        next_turn_is_x = True

        if next_turn_is_x == True:
            playermove = int(input("\nPlayer X: "))
            empty_squares.remove(playermove)
            playerX_moves.append(playermove)
            print(">>> POSITIONS by X: ", playerX_moves)
            print(">>> POSITIONS by 0: ", player0_moves)
            print(">>> Empty ", empty_squares)
            next_turn_is_x = False

        if next_turn_is_x == False:
            playermove = int(input("\nPlayer 0: "))
            empty_squares.remove(playermove)
            player0_moves.append(playermove)
            print(">>> POSITIONS by X: ", playerX_moves)
            print(">>> POSITIONS by 0: ", player0_moves)
            print(">>> Empty ", empty_squares)
            next_turn_is_x = True
            game()

    elif len(empty_squares) == 1:
        playermove = empty_squares[0]
        empty_squares.remove(playermove)
        playerX_moves.append(playermove)
        print(">>> POSITIONS by X: ", playerX_moves)
        print(">>> POSITIONS by 0: ", player0_moves)
        print(">>> Empty ", empty_squares)

    else:
        print("game over")

game()
