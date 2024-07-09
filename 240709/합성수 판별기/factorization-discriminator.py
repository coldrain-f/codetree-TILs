n = int(input())

isComp = False
for i in range(2, n):
    if n % i == 0:
        isComp = True

print("C" if isComp else "N")