s = input()
token = input()

count = 0
for c in s:
    if c == token:
        count += 1
print(count)