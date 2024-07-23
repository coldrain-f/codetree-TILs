arr = list(map(int, input().split()))
count = [0] * 101

for item in arr:
    if item == 0:
        break
    if item >= 1 and item <= 9:
        continue
    if item == 100:
        count[item] += 1
        continue

    count[(item // 10) * 10] += 1

for i in range(100, 9, -10):
    print(f"{i} - {count[i]}")