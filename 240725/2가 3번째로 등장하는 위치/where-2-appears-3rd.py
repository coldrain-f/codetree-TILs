n = int(input())
arr = list(map(int, input().split()))

cnt = 0
for index, item in enumerate(arr):
    if item == 2:
        cnt += 1
    if cnt == 3:
        print(index + 1)
        break