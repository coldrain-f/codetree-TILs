s = input()

for i in range(len(s)):
    if s[i].isalpha():
        print(s[i].lower(), end="")
    if s[i].isdigit():
        print(s[i], end="")