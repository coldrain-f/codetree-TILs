"""
n = 4
공백 3 2 1 0
별 1 3 5 7
"""

n = int(input())
for i in range(n):
    for j in range(i, n - 1):
        print(" ", end=" ")
    for j in range(i * 2 + 1):
        print("*", end=" ")
    print()