_list = [
    input()
    for _ in range(10)
]

ch = input()

for item in _list:
    if item[-1] == ch:
        print(item)