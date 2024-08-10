n = int(input())
_list = [
    [0 for _ in range(n)]
    for _ in range(n)
]

# 첫 번째 행과 첫 번째 열에는 모두 1이 들어갑니다.
for i in range(0, n):
    _list[0][i] = 1
    _list[i][0] = 1

# 나머지 칸들은 바로 위의 값과 바로 왼쪽 값, 그리고 왼쪽 위의 값의 합이 되어야 합니다.
for i in range(1, n):
    for j in range(1, n):
        _list[i][j] = _list[i][j - 1] + _list[i - 1][j] + _list[i - 1][j - 1]

for i in range(n):
    for j in range(n):
        print(_list[i][j], end=" ")
    print()