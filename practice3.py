x = 7
y = 7

for j in range(y):
    for i in range(x):
        if j == 0 or j == y - 1:
            print("*", end="")
        elif j == i:
            print("*", end="")
        elif j + i == x - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
