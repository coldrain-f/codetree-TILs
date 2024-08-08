def convert(s: str) -> int:
    n = ""
    for item in s:
        if not item.isdigit():
            return int(n)
        n += item
    return int(n)

a, b = input().split()
x = y = ""

print(convert(a) + convert(b))