x, y = map(lambda e: (ord(e)), input().split())
print(x * y, x % y if x >= y else y % x)