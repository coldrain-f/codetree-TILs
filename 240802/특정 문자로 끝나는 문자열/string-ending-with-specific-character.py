_list = [
    input()
    for _ in range(10)
]

ch = input()
_count = 0

for item in _list:
    if item[-1] == ch:
        print(item)
        _count += 1

if _count == 0:
    print("None")