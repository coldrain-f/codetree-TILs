n, m = map(int, input().split())

_list1 = [
    list(map(int, input().split()))
    for _ in range(n)
]
_list2 = [
    list(map(int, input().split()))
    for _ in range(n)
]

for i in range(n):
    for j in range(m):
        if _list1[i][j] == _list2[i][j]:
            print(0, end=" ")
        else:
            print(1, end=" ")
    print()