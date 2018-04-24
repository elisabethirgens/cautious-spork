empty_squares = list(range(1,10))
playerX_moves = []
player0_moves = []
winningcombos = [ [1, 2, 3], [4, 5, 6], [7, 8, 9],
[1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

print("""
Let’s play tic-tac-toe! The developer is a newbie python coder 🐍
so for now, plz only type integers from the empty list. 😜
""")

def game_state():
    print(">>> POSITIONS by X: ", playerX_moves)
    print(">>> POSITIONS by 0: ", player0_moves)
    print(">>> Empty ", empty_squares)


def player_wins():
    if set(winningcombos[0]).issubset(playerX_moves) or set(winningcombos[1]).issubset(playerX_moves) or set(winningcombos[2]).issubset(playerX_moves) or set(winningcombos[3]).issubset(playerX_moves) or set(winningcombos[4]).issubset(playerX_moves) or set(winningcombos[5]).issubset(playerX_moves) or set(winningcombos[6]).issubset(playerX_moves) or set(winningcombos[7]).issubset(playerX_moves):
        print(">>> Tic-tac-toe and 🥇  for X")
        exit()

    elif set(winningcombos[0]).issubset(player0_moves) or set(winningcombos[1]).issubset(player0_moves) or set(winningcombos[2]).issubset(player0_moves) or set(winningcombos[3]).issubset(player0_moves) or set(winningcombos[4]).issubset(player0_moves) or set(winningcombos[5]).issubset(player0_moves) or set(winningcombos[6]).issubset(player0_moves) or set(winningcombos[7]).issubset(player0_moves):
        print(">>> Tic-tac-toe and 🥇  for 0")
        exit()


def game():

    if len(empty_squares) > 1:

        next_turn_is_x = True

        if next_turn_is_x == True:
            playermove = int(input("\nPlayer X: "))
            empty_squares.remove(playermove)
            playerX_moves.append(playermove)
            game_state()
            next_turn_is_x = False

        player_wins()

        if next_turn_is_x == False:
            playermove = int(input("\nPlayer 0: "))
            empty_squares.remove(playermove)
            player0_moves.append(playermove)
            game_state()
            next_turn_is_x = True

        player_wins()

        game()

    elif len(empty_squares) == 1:
        playermove = empty_squares[0]
        empty_squares.remove(playermove)
        playerX_moves.append(playermove)
        game_state()

    else:
        print("game over")

game()
