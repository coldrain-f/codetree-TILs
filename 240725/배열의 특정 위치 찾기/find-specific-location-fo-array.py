'''
2 5 8
'''

arr = list(map(int, input().split()))
print(sum(arr[1::2]), end=" ")
length = len(arr[2::3])
avg = sum(arr[2::3]) / length
print(f"{avg:.1f}")