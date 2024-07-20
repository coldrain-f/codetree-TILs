'''
n = 3
0 1    (n - 1)
0 1 2  (n - 0)

n = 5
0 1         i = 2
0 1 2       i = 3
0 1 2 3     i = 4
0 1 2 3 4   i = 5
'''

n = int(input())

for i in range(n):
    for _ in range(i, n):
        print("*", end=" ")
    print()

for i in range(2, n + 1):
    for _ in range(i):
        print("*", end=" ")
    print()