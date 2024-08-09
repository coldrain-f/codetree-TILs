a, b = input().split()
_index = -1

for i in range(len(a)):
    if a[i] == b:
        _index = i
        break

if _index == -1:
    print("No")
else:
    print(_index)