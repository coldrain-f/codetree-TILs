n = int(input())
_list = "".join(input().split())
_count = 0

for i in range(len(_list)):
    print(_list[i], end="")
    _count += 1

    if _count == 5:
        print()
        _count = 0