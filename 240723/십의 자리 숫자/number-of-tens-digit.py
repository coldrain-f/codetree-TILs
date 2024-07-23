arr = list(map(int, input().split()))
count = [0] * 10

for item in arr:
    if item >= 1 and item <= 9:
        continue
    if item == 0:
        break

    count[item // 10] += 1

for i in range(1, 10):
    print(f"{i} - {count[i]}")