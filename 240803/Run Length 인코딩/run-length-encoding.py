'''
count를 새로운 문자가 나올때 까지 센다.
새로운 문자가 나오면 count를 출력하고 0으로 초기화한다.
이를 반복한다.
'''

s = input()
_count = 1
answer = ""

for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        _count += 1
    else:
        answer += s[i - 1] + str(_count)
        _count = 1

answer += s[-1] + str(_count)
print(len(answer))
print(answer)