moves = { }

for i in range(0,9):
    moves[i] = input(">>> ")
    print(f"Player X or 0 said: {moves[i]}")

print('=' * 40)
print(f"{moves}")
