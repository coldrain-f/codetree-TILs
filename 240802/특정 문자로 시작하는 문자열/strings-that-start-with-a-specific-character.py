n = int(input())

_list = [
    input()
    for _ in range(n)
]

ch = input()
_count = 0
acc = 0

for item in _list:
    if item[0] == ch:
        _count += 1
    acc += len(item)

print(f"{_count} {(acc // n):.2f}")