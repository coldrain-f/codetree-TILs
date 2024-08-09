"""
i % 2 == 0이면 list에 append()
문자 카운팅
"""

_count = 0
_list = []

while True:
    s = input()
    if s == '0':
        break
    _count += 1
    if _count % 2 == 1:
        _list.append(s)

print(_count)
print(*_list, sep="\n")