while True:
    x, y, c = input().split()
    x = int(x)
    y = int(y)
    if c == 'c':
        break
    print(x * y)