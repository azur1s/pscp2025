"""gcd"""
a = int(input())
b = int(input())
if b + 1 == 1:
    print(a)
else:
    while b:
        a, b = b, a % b
        if b + 1 == 1:
            print(a)
            break
