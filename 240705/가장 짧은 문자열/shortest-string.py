a = input()
b = input()
c = input()

largest = a
smallest = a
if len(a) > len(b) and len(a) > len(c):
    largest = a
elif len(b) > len(c):
    largest = b
else:
    largest = c

if len(a) < len(b) and len(a) < len(c):
    smallest = a
elif len(b) < len(c):
    smallest = b
else:
    smallest = c

print(len(largest) - len(smallest))