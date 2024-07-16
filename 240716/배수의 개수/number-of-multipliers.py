counts = [0] * 2

for _ in range(10):
    n = int(input())
    if n % 3 == 0:
        counts[0] += 1
    if n % 5 == 0:
        counts[1] += 1

print(counts[0], counts[1])