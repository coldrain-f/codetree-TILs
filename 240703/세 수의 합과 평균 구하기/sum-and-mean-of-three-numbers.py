a, b, c = map(int, input().split())
arr = [a, b, c]
print(sum(arr))
print(f"{sum(arr) // len(arr)}")