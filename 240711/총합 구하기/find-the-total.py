a, b = tuple(map(int, input().split()))

sumVal = 0
for i in range(a, b + 1):
    if i % 6 == 0 and i % 8 != 0:
        sumVal += i

print(sumVal)