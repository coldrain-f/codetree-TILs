n = int(input())
lenAcc = aCount = 0

for _ in range(n):
    data = input()
    lenAcc += len(data)
    if data[0] == 'a':
        aCount += 1

print(lenAcc, aCount)