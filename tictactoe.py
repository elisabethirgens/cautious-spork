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


def player_wins(player, moves):

    if set(winningcombos[0]).issubset(moves) or set(winningcombos[1]).issubset(moves) or set(winningcombos[2]).issubset(moves) or set(winningcombos[3]).issubset(moves) or set(winningcombos[4]).issubset(moves) or set(winningcombos[5]).issubset(moves) or set(winningcombos[6]).issubset(moves) or set(winningcombos[7]).issubset(moves):
        print(">>> Tic-tac-toe and 🥇 for player " + player)
        exit()


def result_draw():
    playerX_moves.append(empty_squares.pop())
    game_state()
    player = 'X'
    player_wins(player, playerX_moves)
    print("\n…and it's a draw. 👌\n")


def game():

    while len(empty_squares) > 1:

        player = 'X'
        playermove = int(input("\nPlayer X: "))
        empty_squares.remove(playermove)
        playerX_moves.append(playermove)
        game_state()
        player_wins(player, playerX_moves)

        player = '0'
        playermove = int(input("\nPlayer 0: "))
        empty_squares.remove(playermove)
        player0_moves.append(playermove)
        game_state()
        player_wins(player, player0_moves)

    result_draw()

game()
