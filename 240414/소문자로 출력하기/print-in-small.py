s = input()

for c in s:
  if not c.isalpha():
    continue
  if ord(c) >= ord('A') and ord(c) <= ord('Z'):
    print(chr(ord(c) + 32), end="")
  else:
    print(c, end="")