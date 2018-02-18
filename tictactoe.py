def game():
    print("Lets play! Only integers between 1-9 plz:")

    for playermove in range(0,9):
        playermove = int(input(">>> "))

        if playermove == 1:
            print("Top left corner, all right. ↖️")
        if playermove == 2:
            print("Top center. ⬆️")
        if playermove == 3:
            print("Top right corner, nice. ↗️")
        if playermove == 4:
            print("Left center. ⬅️")
        if playermove == 5:
            print("Yeah that’s a good one. 🆒")
        if playermove == 6:
            print("Right center. ➡️")
        if playermove == 7:
            print("Bottom left corner, good job. ↙️")
        if playermove == 8:
            print("Bottom center. ⬇️")
        if playermove == 9:
            print("Bottom right corner, cool. ↘️")

game()
