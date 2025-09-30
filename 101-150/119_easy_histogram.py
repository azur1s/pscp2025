"""a"""
s = input(); c = {}
for char in s:
    if char != " ":
        c[char] = c.get(char, 0) + 1
for k in sorted(c.keys(), key=lambda x: (x.lower(), x.isupper())):
    print(f"{k} = {c[k]}")
