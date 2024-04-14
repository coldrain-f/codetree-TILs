x, y = map(ord, input().split())
print(x * y, max(x, y) % min(x, y))