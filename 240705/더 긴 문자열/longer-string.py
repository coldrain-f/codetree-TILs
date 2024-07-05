names = input().split()

if len(names[0]) > len(names[1]):
    print(names[0], len(names[0]))
elif len(names[1]) > len(names[0]):
    print(names[1], len(names[1]))
else:
    print("same")