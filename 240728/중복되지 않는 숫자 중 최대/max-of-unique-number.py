'''
원소가 1~1000 범위 이므로 -1로 초기화 해도 된다.
카운팅 배열을 활용하여 중복하여 등장하는 숫자 체크
'''

_count = [0] * 1001
largest = -1
n = int(input())
_list = list(map(int, input().split()))

for item in _list:
    _count[item] += 1

for item in _list:
    if _count[item] > 1:
        continue
    if item > largest:
        largest = item

print(largest)