n = int(input())

sum = 0
for _ in range(n):
    m = int(input())
    if m % 2 == 1 and m % 3 == 0:
        sum += m

print(sum)