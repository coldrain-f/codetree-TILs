def isPrime(n: int) -> bool:
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = int(input())
if isPrime(n):
    print("P")
else:
    print("C")