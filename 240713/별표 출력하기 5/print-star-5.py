n = int(input())

# 2
# 1

for i in range(n):
    for _ in range(n - i):
        for _ in range(n - i):
            print("*", end="")
        print(end=" ")
    print()