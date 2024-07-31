"""
열고정 행변화
행이 i % 2 == 1이라면 위로 이동
행이 i % 2 == 0이라면 아래로 이동
"""
n = int(input())

_list = [
    [0 for _ in range(n)]
    for _ in range(n)
]

inc = 1
for i in range(n - 1, -1, -1):
    if i % 2 == 1:
        for j in range(n - 1, -1, -1):
            _list[j][i] = inc
            inc += 1
    else:
        for j in range(n):
            _list[j][i] = inc
            inc += 1

for i in range(n):
    for j in range(n):
        print(_list[i][j], end=" ")
    print()