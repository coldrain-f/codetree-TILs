n, m = map(int, input().split())
_list = [
    [0 for _ in range(m)]
    for _ in range(n)
]

inc = 1
for i in range(n):
    for j in range(m):
        _list[i][j] = inc
        inc += 1

for i in range(n):
    for j in range(m):
        print(_list[i][j], end=" ")
    print()