s = list(input())

while len(s) > 1:
    _index = int(input())

    if _index >= len(s):
        s.pop(len(s) - 1)
    else:
        s.pop(_index)
        
    print(*s, sep="")