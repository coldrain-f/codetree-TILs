'''
i % 2 == 0이면 * 1개
i % 2 == 1이면 * i + 1개
'''
n = int(input())

for i in range(n): # 0-1-2-3
    if i % 2 == 0:
        print("*", end=" ")
    else:
        for j in range(i + 1):
            print("*", end=" ")
    print()