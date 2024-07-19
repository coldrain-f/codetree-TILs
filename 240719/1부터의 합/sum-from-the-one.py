n = int(input())

sumVal = 0

for i in range(1, 101):
    sumVal += i
    if sumVal >= n:
        print(i)
        break