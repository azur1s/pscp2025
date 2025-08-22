"""a"""
while True:
    n = int(input())
    if not n:
        break
    COUNT = 1
    while n > 1:
        if not n % 2:
            n //= 2
        else:
            n *= 3
            n += 1
        COUNT += 1
    print(COUNT)
