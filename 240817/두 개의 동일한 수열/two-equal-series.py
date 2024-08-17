n = int(input())
_list1 = list(map(int, input().split()))
_list2 = list(map(int, input().split()))
_list1.sort()
_list2.sort()

answer = "Yes"
for i in range(n):
    if _list1[i] != _list2[i]:
        print("No")
        break

print(answer)