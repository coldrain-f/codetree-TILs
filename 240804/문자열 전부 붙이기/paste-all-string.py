n = int(input())
answer = ""

_list = [
    input()
    for _ in range(n)
]

for i in range(len(_list)):
    answer += _list[i]

print(answer)