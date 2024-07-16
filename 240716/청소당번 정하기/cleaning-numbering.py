'''
2일마다 교실 청소
3일마다 복도 청소
12일마다 화장실 청소

날짜가 겹치면 주기가 더 긴 것을 하기로 한다.

풀이)
n일 마다? n으로 나누어 떨어지면 n일마다가 된다.
'''

n = int(input())
counts = [0] * 3

for i in range(1, n + 1):
    if i % 12 == 0:
        counts[2] += 1
    elif i % 3 == 0:
        counts[1] += 1
    elif i % 2 == 0:
        counts[0] += 1
    
print(*counts)