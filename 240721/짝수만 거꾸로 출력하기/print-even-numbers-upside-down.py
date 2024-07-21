n = int(input())
arr = list(map(int, input().split()))

even = []
for item in arr:
    if item % 2 == 0:
        even.append(item)

print(*even[::-1])