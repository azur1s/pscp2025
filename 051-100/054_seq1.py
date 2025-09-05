"""a"""
m = int(input())
n = int(input())

X = 0
for a in range(m):
    a = a + 1
    for i in range(n):
        X += 1
        if i == n - 1:
            print(X)
        else:
            print(X, end=' ')
