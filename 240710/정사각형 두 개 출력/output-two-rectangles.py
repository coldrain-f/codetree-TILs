def printStar(n: int) -> None:
    for _ in range(n):
        for _ in range(n):
            print("*", end="")
        print()

n = int(input())

printStar(n)
print()
printStar(n)