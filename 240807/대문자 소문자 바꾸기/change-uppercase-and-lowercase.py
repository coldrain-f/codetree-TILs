s = input()

for item in s:
    if item.islower():
        print(item.upper(), end="")
    elif item.isupper():
        print(item.lower(), end="")