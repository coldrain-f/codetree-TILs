n = int(input())

count = 0
for i in range(1, n + 1):
    if i % 100 == 0 and i % 400 != 0:
        continue
    if i % 4 != 0:
        continue
    count += 1 

print(count)