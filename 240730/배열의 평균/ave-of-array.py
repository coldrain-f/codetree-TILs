_list = []
xSum = [0] * 2
ySum = [0] * 4

for _ in range(2):
    data = list(map(int, input().split()))
    _list.append(data)

for i in range(2):
    for j in range(4):
        xSum[i] += _list[i][j]
    
for i in range(4):
    for j in range(2):
        ySum[i] += _list[j][i]

for i in range(2):
    print(f"{(xSum[i] / 4):.1f}", end=" ")
print()
for i in range(4):
    print(f"{(ySum[i] / 2):.1f}", end=" ")
print()
print(f"{(sum(xSum) / 8):.1f}")