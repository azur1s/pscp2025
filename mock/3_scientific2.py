"""a"""
def count_trailing_zeros(s):
    """a"""
    n = 0
    is_dp = False
    encounter_non_zero = False

    for i in range(len(s)):
        ch = s[-(i + 1)]
        if ch == "0" and not encounter_non_zero:
            n += 1
        elif ch == ".":
            is_dp = True
        else:
            encounter_non_zero = True

    return n if is_dp else 0

def m():
    """a"""
    a = input()

    try:
        float(a)
        isnum = True
    except ValueError:
        isnum = False

    if isnum:
        NEG = True if a[0] == "-" else False
        if NEG:
            a = a[1:]

        n = float(a)
        if not n:
            print(0)
            return
        X = 0
        DEC = False
        if n < 1.0:
            DEC = True
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
        if not X:
            print(0)
        else:
            print(f"{"-" if NEG else ""}{n}{"0" * count_trailing_zeros(a)} x 10^{"-" if DEC else ""}{X}")
    else:
        for line in a.replace(" x ", "\n"):
            print(line)
        # b = float(b[3:])
        # r = float(a) * pow(10, b)
        # if int(r) == r:
        #     print(int(r))
        # else:
        #     print(r)

m()
