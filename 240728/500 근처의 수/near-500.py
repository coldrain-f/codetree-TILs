_list = list(map(int, input().split()))

largest = float("-inf")
smallest = float("inf")

for item in _list:
    if item < 500 and item > largest:
        largest = item
    if item > 500 and item < smallest:
        smallest = item

print(largest, smallest)