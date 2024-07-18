n = int(input())

# 모두 만족하지 않으면 온전수라는 말은
# 다르게 말해서 하나라도 만족하면 온전수가 아니라는 말이다.
for i in range(1, n + 1):
    if i % 2 == 0 or i % 10 == 5 or (i % 3 == 0 and i % 9 != 0):
        continue
    print(i, end=" ")