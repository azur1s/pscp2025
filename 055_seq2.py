"""a"""
x = int(input())

for i in range(x):
    print(" ".join(str((y * x) + i) for y in range(x)))
