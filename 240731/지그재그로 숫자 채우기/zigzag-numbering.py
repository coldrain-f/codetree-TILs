'''
열고정 행변화
행이 i % 2 == 0이면 아래로
i % 2 == 1이면 위로
'''

n, m = tuple(map(int, input().split()))

_list = [
    [0 for _ in range(m)]
    for _ in range(n)
]

inc = 0
for i in range(m):
    if i % 2 == 0:
        for j in range(n):
            _list[j][i] = inc
            inc += 1
    else:
        for j in range(n - 1, -1, -1):
            _list[j][i] = inc
            inc += 1

for i in range(n):
    for j in range(m):
        print(_list[i][j], end=" ")
    print()