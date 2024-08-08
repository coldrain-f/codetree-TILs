x, y = map(int, input().split())
z = x + y

_count = 0
for item in str(z):
    if item == '1':
        _count += 1

print(_count)