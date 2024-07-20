'''
n = 4
0        i + 1
0 1
0 1 2
0 1 2 3

0 1 2    0일때 3
0 1      1일때 3
0        2일때
i부터 n - 1까지
'''

n = int(input())

for i in range(n):
    for _ in range(i + 1):
        print("*", end="")
    print("\n")

for i in range(n - 1):
    for _ in range(i, n - 1):
        print("*", end="")
    print("\n")