s = input()

s = list(s)
s[1] = s[-2] = 'a'
print(*s, sep="")