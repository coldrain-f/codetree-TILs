n = int(input())

for i in range(n, 101):
    rank = ""
    if i >= 90:
        rank = "A"
    elif i >= 80:
        rank = "B"
    elif i >= 70:
        rank = "C"
    elif i >= 60:
        rank = "D"
    else:
        rank = "F"
    print(rank, end=" ")