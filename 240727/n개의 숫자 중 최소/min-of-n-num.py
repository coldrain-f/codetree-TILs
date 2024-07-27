n = int(input())
_list = list(map(int, input().split()))
smallest = float("inf")

for item in _list:
    if item < smallest:
        smallest = item

print(smallest, _list.count(smallest))