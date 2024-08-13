"""
n = 2
i * 2 + 1 
(i = 1일 때 3개)
(i = 0일 때 1개) i 역순으로
공백은 0 1 2

4 4부터 4보다 작을 때까지
3 3부터 4보다 작을 때까지
2 2부터 4보다 작을 때까지
1 1부터 4보다 작을 때까지 

"""

n = int(input())

for i in range(n - 1, -1, -1):
    for j in range(i + 1, n):
        print(" ", end=" ")
    for j in range(i * 2 + 1):
        print("*", end=" ")
    print()


"""
2 1일떄 3보다 작을때 까지
1 2일때 3보다 작을떄 까지
0 3일때 3보다 작을때 까지
"""

for i in range(1, n):
    for j in range(i, n - 1):
        print(" ", end=" ")
    for j in range(i * 2 + 1):
        print("*", end=" ")
    print()