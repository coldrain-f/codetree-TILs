'''
0: A
1: B
2: C
3: D
'''
count = [0] * 4

for _ in range(3):
    s, t = input().split()
    t = int(t)
    if s == "Y":
        if t >= 37:
            count[0] += 1 # A
        else:
            count[2] += 1 # C
    else:
        if t >= 37:
            count[1] += 1 # B
        else:
            count[3] += 1 # D

print(*count, end=" ")
print("E" if count[0] >= 2 else "")