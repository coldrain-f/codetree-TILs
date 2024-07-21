n = int(input())

for i in range(n - 1, -1, -1):
    for _ in range(i, n - 1):
        print(" ", end=" ")
    for _ in range(0, i * 2 + 1):
        print("*", end=" ")
    print()