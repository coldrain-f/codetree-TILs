sumVal = 0
count = 0
while True:
    n = int(input())
    if n < 20 or n > 29:
        break
    sumVal += n
    count += 1

print(f"{(sumVal / count):.2f}")