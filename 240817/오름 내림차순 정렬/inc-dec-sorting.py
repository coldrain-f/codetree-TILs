n = int(input())
_list = list(map(int, input().split()))

print(*sorted(_list))
print(*sorted(_list, reverse=True))