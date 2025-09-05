"""a"""
x = input()
a = sum(int(ch) for ch in x)
b = sum(int(ch) * (10 ** (i + 1)) for i, ch in enumerate(reversed(x[10:])))
c = a + b

if c < 1000:
    c += 1000
    print(c)
elif c >= 10000:
    print(str(c)[1:])
else:
    print(c)
