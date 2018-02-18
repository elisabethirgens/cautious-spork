def game():
    moves = { }
    i = 1

    while len(moves) < 8:
        moves[i] = input("X >>> ")
        print(f"Player X: {moves[i]}")
        i += 1
        moves[i] = input("0 >>> ")
        print(f"Player 0: {moves[i]}")
        i += 1

    print('=' * 40)
    print(f"{moves}")

game()
