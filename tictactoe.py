def game():
    moves = { }
    i = 1

    while i <= 9:
        moves[i] = input(">>> ")
        print(f"Player X or 0 said: {moves[i]}")
        i += 1

    print('=' * 40)
    print(f"{moves}")

game()
