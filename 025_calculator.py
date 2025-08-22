"""a"""
n = int(input())
if n == 1:
    print(1)
else:
    C = 0
    for i in range(n):
        C += len(str(i + 1)) + 1
    print(C)
