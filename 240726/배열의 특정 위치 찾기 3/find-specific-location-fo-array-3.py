'''
문제 특성상 0은 무조건 있다.
→ 원소가 있는지 확인하지 않고 index() 함수 사용
'''

arr = list(map(int, input().split()))
idx = arr.index(0)

print(arr[idx - 1] + arr[idx - 2] + arr[idx - 3])