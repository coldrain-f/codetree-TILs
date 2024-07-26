'''
홀수번째: 0, 2, 4, 6...
짝수번째: 1, 3, 5, 7...
인덱스 % 2 == 0 홀수번째
인덱스 % 2 == 1 짝수번째
'''
arr = list(map(int, input().split()))

odd, even = 0, 0
for index, item in enumerate(arr):
    if index % 2 == 0:
        odd += item
    else:
        even += item

print(max([odd, even]) - min([odd, even]))