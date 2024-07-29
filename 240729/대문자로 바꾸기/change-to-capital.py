_list = []
for _ in range(5):
    data = input().split()
    _list.append(data)

for i in range(5):
    for j in range(3):
        print(_list[i][j].upper(), end=" ")
    print()