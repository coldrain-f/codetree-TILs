_list1 = [
    list(map(int, input().split()))
    for _ in range(3)
]
input()
_list2 = [
    list(map(int, input().split()))
    for _ in range(3)
]

for i in range(3):
    for j in range(3):
        print(_list1[i][j] * _list2[i][j], end=" ")
    print()