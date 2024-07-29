n = int(input())
_list = list(map(int, input().split()))
largest = float("-inf")

for i in range(n - 1):
    for j in range(i + 1, n):
        if _list[j] < _list[i]:
            continue
        diff = _list[j] - _list[i]
        if diff > largest:
            largest = diff

print(0 if largest == float("-inf") else largest)