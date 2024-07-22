n = int(input())
arr = list(map(int, input().split()))
even = []

# 짝수를 새로운 배열에 저장 후 출력
for item in arr:
    if item % 2 == 0:
        even.append(item)

print(*even)