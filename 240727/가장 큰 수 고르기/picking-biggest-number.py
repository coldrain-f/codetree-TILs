_list = list(map(int, input().split()))
largest = float("-inf")

for item in _list:
    if item > largest:
        largest = item

print(largest)