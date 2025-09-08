"""a"""
m = int(input())
n = int(input())
ms = set(input() for _ in range(m))
ns = set(input() for _ in range(n))
dups = ms & ns
print("Nope" if not dups else "\n".join(reversed(sorted(dups))))
