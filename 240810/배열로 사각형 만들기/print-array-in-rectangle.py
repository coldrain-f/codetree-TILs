_list = [
    [0 for _ in range(5)]
    for _ in range(5)
]

# 1. 첫 번째 행과 첫 번째 열은 모두 1로 초기화 합니다.
for i in range(0, 5):
    _list[0][i] = 1
    _list[i][0] = 1

# 2. 나머지 칸들은 바로 위의 값과 바로 왼쪽의 값을 더합니다.
for i in range(1, 5):
    for j in range(1, 5):
        _list[i][j] = _list[i - 1][j] + _list[i][j - 1]

for i in range(5):
    for j in range(5):
        print(_list[i][j], end=" ")
    print()