s = input()
acc = 0

for i in range(len(s)):
    if not s[i].isdigit():
        continue
    acc += ord(s[i]) - 48

print(acc)