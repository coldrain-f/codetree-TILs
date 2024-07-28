n = int(input())
_list = list(map(int, input().split()))

first = second = float("-inf")

# 가장 큰 값 찾기
for item in _list:
    if item > first:
        first = item

# 가장 큰 값 제거
_list.remove(first)

# 두번째로 큰 값 찾기
for item in _list:
    if item > second:
        second = item

print(first, second)