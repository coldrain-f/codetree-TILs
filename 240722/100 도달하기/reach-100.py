n = int(input())

arr = [1, n]
i = 1
while True:
    i += 1
    arr.append(arr[i - 2] + arr[i - 1])
    if arr[i] >= 100:
        break

print(*arr)