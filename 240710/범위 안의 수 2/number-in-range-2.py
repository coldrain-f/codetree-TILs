sum = 0
count = 0
for _ in range(10):
    n = int(input())
    if n >= 0 and n <= 200:
        sum += n
        count += 1

if count >= 1:
    print(f"{sum} {(sum / count):.1f}")