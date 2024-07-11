n = int(input())

sumVal = 0
for _ in range(n):
    m = int(input())
    sumVal += m

print(f"{sumVal} {(sumVal / n):.1f}")