'''
0
0 1
0 1 2
0 1 2 3 
'''
_list = [
    list(map(int, input().split()))
    for _ in range(4)
]
acc = 0

for i in range(4):
    for j in range(0, i + 1):
        acc += _list[i][j]

print(acc)