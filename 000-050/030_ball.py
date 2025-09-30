"""a"""
x = float(input())
C = 0
while True:
    x *= 0.6
    if x > 0.01:
        C += 1
    else:
        break
print(C)
