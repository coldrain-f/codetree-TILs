_list = list(map(int, input().split()))
smallest = float("inf")
largest = float("-inf")

for item in _list:
    if item == 999 or item == -999:
        print(largest, smallest)
        break
    if item < smallest:
        smallest = item
    if item > largest:
        largest = item