"""a"""
n = int(input())
xs = []
for x in range(n):
    x = x + 1 # please kys pep8
    xs.append(input())
print("\n".join(sorted(xs, key=lambda x: (len(x), x))))
