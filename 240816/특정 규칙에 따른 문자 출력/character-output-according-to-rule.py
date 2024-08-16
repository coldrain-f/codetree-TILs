'''
n = 3
공백 2-1-0
@ 1-2-3
'''

n = int(input())

for i in range(n): # 0-1-2
    for j in range(i, n - 1):
        print(" ", end=" ")
    for j in range(i + 1):
        print("@", end=" ")
    print()

for i in range(n - 1): # 0-1
    for j in range(i, n - 1):
        print("@", end=" ")
    print()