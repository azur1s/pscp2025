"""n"""
a = input()

def count_trailing_zeros(s):
    i = 0
    n = 0

    while True:
        ch = s[-(i + 1)]
        if ch == "0":
            n += 1
            i += 1
        elif ch == ".":
            n += 1
            break
        else:
            break

    return n

X = 0
try:
    n = float(a)
    NEG = False
    if n < 1.0:
        NEG = True
        while True:
            if 0 < n < 1.0:
                X += 1
                n = n * 10
            else:
                break
    else:
        while True:
            if n >= 10.0:
                X += 1
                n = n / 10
            else:
                break
    tz = "0" * count_trailing_zeros(a)
    print(f"{n}{tz} x 10^{X}")
except ValueError:
    print("bogus")