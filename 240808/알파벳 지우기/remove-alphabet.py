def convert(s: str) -> int:
    n = ""
    for item in s:
        if item.isdigit():
            n += item
    return int(n)

_list = [
    input()
    for _ in range(2)
]

print(sum([convert(_list[0]), convert(_list[1])]))