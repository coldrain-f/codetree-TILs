# 윤년인 경우
# 평년인 경우 - 2가지 경우이므로 이를 묶는것이 편하다.

y = int(input())

if (y % 100 == 0 and y % 400 != 0) or (y % 4 != 0):
    print("false")
else:
    print("true")