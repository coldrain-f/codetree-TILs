n = int(input())

def is369(n: int) -> bool:
    if n % 3 == 0:
        return True
    while n > 0:
        if n in {3, 6, 9}:
            return True
        n //= 10
    return False

for i in range(1, n + 1):
    if is369(i):
        print(0, end=" ")
    else:
        print(i, end=" ")