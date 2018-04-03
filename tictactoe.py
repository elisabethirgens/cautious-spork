empty_squares = [1, 2, 3, 4, 5, 6, 7, 8, 9]
playerX_moves = []
player0_moves = []
winningcombo_1 = [1, 2, 3]
winningcombo_2 = [4, 5, 6]
winningcombo_3 = [7, 8, 9]
winningcombo_4 = [1, 4, 7]
winningcombo_5 = [2, 5, 8]
winningcombo_6 = [3, 6, 9]
winningcombo_7 = [1, 5, 9]
winningcombo_8 = [3, 5, 7]

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

        if set(winningcombo_1).issubset(playerX_moves) or set(winningcombo_2).issubset(playerX_moves) or set(winningcombo_3).issubset(playerX_moves) or set(winningcombo_4).issubset(playerX_moves) or set(winningcombo_5).issubset(playerX_moves) or set(winningcombo_6).issubset(playerX_moves) or set(winningcombo_7).issubset(playerX_moves) or set(winningcombo_8).issubset(playerX_moves):
            print(">>> Tic-tac-toe and 🥇  for X")
            return

        if next_turn_is_x == False:
            playermove = int(input("\nPlayer 0: "))
            empty_squares.remove(playermove)
            player0_moves.append(playermove)
            print(">>> POSITIONS by X: ", playerX_moves)
            print(">>> POSITIONS by 0: ", player0_moves)
            print(">>> Empty ", empty_squares)
            next_turn_is_x = True

        if set(winningcombo_1).issubset(player0_moves) or set(winningcombo_2).issubset(player0_moves) or set(winningcombo_3).issubset(player0_moves) or set(winningcombo_4).issubset(player0_moves) or set(winningcombo_5).issubset(player0_moves) or set(winningcombo_6).issubset(player0_moves) or set(winningcombo_7).issubset(player0_moves) or set(winningcombo_8).issubset(player0_moves):
            print(">>> Tic-tac-toe and 🥇  for 0")
            return

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
