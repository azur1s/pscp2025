"""a"""
n = int(input())
xs = [input() for _ in range(n)]

def check(s):
    """a"""
    buf = ""
    i = 0
    while True:
        if i >= len(s):
            break
        buf += s[i]
        i += 1

        if buf == "ba" and len(s) - i >= 3 and s[i:i+3] == "kka":
            buf = ""
            i += 3
        elif buf == "ba" and len(s) - i >= 2 and s[i:i+2] == "ka":
            return False

        if buf in ("ka", "ba", "ta"):
            buf = ""
    return buf == ""

for x in xs:
    print("yes" if check(x) else "no")