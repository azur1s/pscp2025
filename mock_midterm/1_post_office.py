"""a"""
n_envelopes = int(input())
n_packages = int(input())

TOTAL = 0

for i in range(n_envelopes):
    i = i + 1 # pep8, ignore
    w = float(input())
    TOTAL += 13
    if w <= 10:
        TOTAL += 16
    elif w <= 20:
        TOTAL += 18
    elif w <= 100:
        TOTAL += 23
    elif w <= 250:
        TOTAL += 28
    elif w <= 500:
        TOTAL += 33
    elif w <= 1000:
        TOTAL += 48
    else:
        TOTAL += 68

for i in range(n_packages):
    i = i + 1 # pep8, ignore
    w = float(input())
    TOTAL += 15
    if w <= 500:
        TOTAL += 45
    elif w <= 1000:
        TOTAL += 55
    else:
        TOTAL += 70

print(TOTAL)
