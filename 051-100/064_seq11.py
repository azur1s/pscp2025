"""a"""
n = int(input())
xs = [i + 1 for i in range(n)] + [i + 1 for i in reversed(range(n - 1))]
print(xs)
