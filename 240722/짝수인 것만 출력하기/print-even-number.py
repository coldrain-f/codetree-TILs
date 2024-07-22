n = int(input())
arr = list(map(int, input().split()))
even = []

even = filter(lambda item : item % 2 == 0, arr)
print(*even)