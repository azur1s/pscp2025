"""a"""

n = int(input())

xs = []
while True:
    x = int(input())
    if not x:
        break
    xs.append(x)

full = set(range(1, n + 1))
missing = sorted(list(full - set(xs)))

for m in missing:
    print(m)
