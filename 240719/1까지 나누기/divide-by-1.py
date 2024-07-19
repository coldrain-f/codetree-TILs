n = int(input())

i = 1
count = 0
while n > 1:
    n //= i
    count += 1
    i += 1

print(count)