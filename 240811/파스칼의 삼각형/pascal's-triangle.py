"""
시작점과 끝점은 모두 1
그 이외에는 왼쪽 대각선위 + 위로 나타낸다.
"""

n = int(input())
_list = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for i in range(n):
    for j in range(0, i + 1):
        if i == j or j == 0:
            _list[i][j] = 1
        else:
            _list[i][j] = _list[i - 1][j - 1] + _list[i - 1][j]

for i in range(n):
    for j in range(0, i + 1):
        print(_list[i][j], end=" ")
    print()