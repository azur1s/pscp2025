"""a"""
s = input()
c = {}
for char in s:
    if char.isalpha():
        c[char] = c.get(char, 0) + 1
maxh = max(c.values())
c = dict(sorted(c.items()))

for i in range(maxh, 0, -1):
    print(str(i).rjust(2), end="  ")
    S = ""
    for k in c:
        if c[k] >= i:
            S += "* "
        else:
            S += "  "
    print(S.rstrip())

print("    ", end="")
S1 = ""
for k in c:
    # print(k, end=" " if l < len(c) - 1 else "")
    S1 += f"{k} "
print(S1.rstrip())
