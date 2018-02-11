print("Welcome! Let’s play a game of tic-tac-toe.")

moves = { }

for i in range(0,9):
    playermove = input(">>> ")
    print(f"Player X or 0 said: {playermove}")
    moves[i] = playermove

print("Done! Sry, I have no idea yet if anyone won.")
print('=' * 40)
print("But look! Here are your moves:")
print(f"{moves}")
print('=' * 40)
