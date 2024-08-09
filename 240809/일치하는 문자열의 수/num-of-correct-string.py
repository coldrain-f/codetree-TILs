n, a = input().split()
n = int(n)

_count = 0
for _ in range(n):
    s = input()
    if s == a:
        _count += 1

print(_count)