n = int(input())

# 자기 자신을 제외한 약수의 합이 자신이 되는 수
# 자기 자신을 제외한 약수를 구한다.
# 약수를 누적한다.
# 완전수인지 판단한다.

sum = 0
for i in range(1, n):
    if n % i == 0:
        sum += i

if sum == n:
    print("P")
else:
    print("N")