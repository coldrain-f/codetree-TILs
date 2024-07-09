a, b = map(int, input().split())

isDivisor = False

for i in range(a, b + 1):
    if 1920 % i == 0 and 2880 % i == 0:
        isDivisor = True

print(int(isDivisor))