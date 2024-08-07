def isAlpha(ch: str) -> bool:
    if ch >= 'a' and ch <= 'z':
        return True
    if ch >= 'A' and ch <= 'Z':
        return True
    return False

def toUpperCase(ch: str) -> str:
    if ch >= 'a' and ch <= 'z':
        return chr(ord(ch) - 32)
    return ch

s = input()

for i in range(len(s)):
    if isAlpha(s[i]):
        print(toUpperCase(s[i]), end="")