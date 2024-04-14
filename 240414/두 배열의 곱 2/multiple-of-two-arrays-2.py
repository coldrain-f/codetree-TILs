matrix1, matrix2 = [], []

for _ in range(4):
  data = list(map(int, input().split()))
  matrix1.append(data)
input()
for _ in range(4):
  data = list(map(int, input().split()))
  matrix2.append(data)
  
for i in range(4):
  for j in range(2):
    print(matrix1[i][j] * matrix2[i][j], end=" ")
  print()