moves = []

def game():
    print("Lets play! Only integers between 1-9 plz:")

    for playermove in range(0,9):
        playermove = int(input(">>> "))
        moves.append(playermove)

game()

print(moves)
