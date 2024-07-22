n = int(input())
m = count = 0

while True:
    m = m + n
    print(m, end=" ")

    if m % 5 == 0:
        count += 1
    if count >= 2:
        break