n = int(input())

for i in range(1, n + 1):
    satisfied = False
    m = i
    while m > 0:
        digit = m % 10
        if digit == 3 or digit == 6 or digit == 9:
            satisfied = True
        m //= 10
    if satisfied:
        print(0, end=" ")
    else:
        print(i, end=" ")