"""a"""

m = int(input())
n = int(input())

mat = []
for i in range(m):
    i = i + 1
    row = [input() for _ in range(n)]
    mat.append(row)

for row in mat:
    print(" ".join(row))
