n, m = map(int, input().split())
_list = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for _ in range(m):
    r, c = map(int, input().split())
    _list[r - 1][c - 1] = 1

for i in range(n):
    for j in range(n):
        print(_list[i][j], end=" ")
    print()