_list = ["apple", "banana", "grape", "blueberry", "orange"]
_count = 0

ch = input()

for item in _list:
    if item[2] == ch or item[3] == ch:
        print(item)
        _count += 1

print(_count)