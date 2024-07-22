arr = map(int, input().split())

for item in arr:
    if item == 0:
        break
    if item % 2 == 0:
        item //= 2
    else:
        item += 3

    print(item, end=" ")