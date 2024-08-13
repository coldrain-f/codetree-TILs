"""
n = 3
0 * 2 + 1 = 1, 0부터 3 - 1보다 작을 때까지 2
1 * 2 + 1 = 3, 1부터 3 - 1보다 작을 때까지 1
2 * 2 + 1 = 5, 2부터 3 - 1보다 작을 떄까지 0

1 * 2 + 1, 1부터 3 - 1보다 작을 떄까지 1
0 * 2 + 1, 0부터 3 - 1보다 작을 떄까지 2
"""

n = int(input())

for i in range(n):
    for j in range(i, n - 1):
        print(" ", end="")
    for j in range(i * 2 + 1):
        print("*", end="")
    print()

for i in range(n - 2, -1, -1):
    for j in range(i, n - 1):
        print(" ", end="")
    for j in range(i * 2 + 1):
        print("*", end="")
    print()