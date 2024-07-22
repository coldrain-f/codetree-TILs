n = int(input())

# 넉넉하게 20개 정도로 잡는다.
arr = [0] * 20
arr[0] = 1
arr[1] = n

print(arr[0], arr[1], end=" ")

for i in range(2, 20):
    arr[i] = arr[i - 2] + arr[i - 1]
    print(arr[i], end=" ")
    if arr[i] >= 100:
        break