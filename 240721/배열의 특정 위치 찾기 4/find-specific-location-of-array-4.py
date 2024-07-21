arr = list(map(int, input().split()))

count = 0
acc = 0

for item in arr:
    if item is 0:
        break
    if item % 2 == 0:
        count += 1
        acc += item

print(count, acc)