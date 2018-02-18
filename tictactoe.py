def game():

    moves = [ ]

    while len(moves) < 8:
        playermove = input("X >>> ")
        print(f"Player X: {playermove}")
        moves.append(playermove)
        playermove = input("0 >>> ")
        print(f"Player 0: {playermove}")
        moves.append(playermove)

    print(f"{moves}")

game()
