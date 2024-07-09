c1, t1 = input().split()
c2, t2 = input().split()
c3, t3 = input().split()

t1 = int(t1)
t2 = int(t2)
t3 = int(t3)

count = 0
if c1 == "Y":
    if t1 >= 37:
        count += 1
if c2 == "Y":
    if t2 >= 37:
        count += 1
if c3 == "Y":
    if t3 >= 37:
        count += 1

if count >= 2:
    print("E")
else:
    print("N")