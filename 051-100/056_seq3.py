"""a"""
x = int(input())

for i in range(x):
    print(" ".join(str(y + i + 2) for y in range(x)))
