s = list(input())
s.pop(1)
s.pop(len(s) - 2)

print(*s, sep="")