a, b, c = map(int, input().split())

smallest = min([a, b, c])
print(int(a == smallest), end=" ")
print(int(a == b and b == c))