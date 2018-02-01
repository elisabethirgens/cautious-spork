print("Welcome! Let’s play a game of tic-tac-toe.")

moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for playermove in moves:
    playermove = input(">: ")
    print(f"Player X or 0 said: {playermove}")

print("Done! Sry, I have no idea yet if anyone won.")
