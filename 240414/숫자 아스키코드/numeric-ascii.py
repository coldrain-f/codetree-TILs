n = int(input())

for _ in range(n):
  alpha = input()
  
  if alpha.isalpha():
    print(alpha)
  elif alpha.isdigit():
    print(ord(alpha))