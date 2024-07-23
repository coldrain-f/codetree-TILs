n = int(input())
numbers = list(map(int, input().split()))
count = [0] * 10

for number in numbers:
    count[number] += 1

for item in count:
    print(item)