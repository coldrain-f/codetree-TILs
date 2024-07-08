math1, eng1 = map(int, input().split())
math2, eng2 = map(int, input().split())

if math1 > math2:
    print("A")
elif math2 > math1:
    print("B")
elif eng1 > eng2:
    print("A")
else:
    print("B")