"""
n = 3
1개 2개 3개
2개 1개
"""
n = int(input())

for i in range(n): # 2 1 0
    for j in range(i, n - 1):
        print(" ", end="")
    for j in range(i + 1):
        print("*", end=" ")
    print()

for i in range(n - 1, 0, -1): # 2 1
    for j in range(i, n):
        print(" ", end="")
    for j in range(0, i):
        print("*", end=" ")
    print()