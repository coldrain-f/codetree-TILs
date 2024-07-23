a, b = map(int, input().split())
count = [0] * 10
acc = 0

while a > 1:
    r = a % b
    a = a // b
    count[r] += 1

for i in range(10):
    acc += count[i] ** 2

print(acc)