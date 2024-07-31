"""
열고정 행변화
"""

n = int(input())
_list = [
    [0 for _ in range(n)]
    for _ in range(n)
]

inc = 1
for i in range(n):
    for j in range(n):
        _list[j][i] = inc
        inc += 1

for i in range(n):
    for j in range(n):
        print(_list[i][j], end=" ")
    print()