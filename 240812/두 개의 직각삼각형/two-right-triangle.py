"""
n = 4
별 4-3-2-1
공백 0-2-4-6
별 4-3-2-1
"""
n = int(input())

for i in range(n):
    for j in range(i, n):
        print("*", end="")
    for j in range(i * 2):
        print(" ", end="")
    for j in range(i, n):
        print("*", end="")
    print()