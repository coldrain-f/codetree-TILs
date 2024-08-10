n = int(input())
acc = 0
for _ in range(n):
    digit = int(input())
    acc += digit

acc = str(acc)
# 2077
acc = acc[1:] + acc[0]
print(acc)