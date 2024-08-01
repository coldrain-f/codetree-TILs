_list = [
    input()
    for _ in range(4)
]

print(*_list[::-1], sep="\n")