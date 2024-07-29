n = int(input())
_list = list(map(int, input().split()))
smallest = float("inf")

for i in range(n - 1):
    for j in range(i + 1, n):
        diff = _list[j] - _list[i]
        if diff < smallest:
            smallest = diff

print(smallest)