"""a"""
x = int(input())

for i in range(x):
    print(" ".join(str(y + 1 + (i * x)) for y in range(x)))
