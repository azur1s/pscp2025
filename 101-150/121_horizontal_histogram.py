"""a"""
s = input()
c = {}
for x in s:
    c[x] = c.get(x, 0) + 1
for k in sorted(c, key=lambda x: (x.isupper(), x)):
    print(k, ":", ("-" * c[k]).replace("-----", "-----|").strip("|"))
