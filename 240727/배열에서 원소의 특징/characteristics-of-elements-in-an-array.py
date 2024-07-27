_list = list(map(int, input().split()))

for index, item in enumerate(_list):
    if item % 3 == 0:
        print(_list[index - 1])
        break