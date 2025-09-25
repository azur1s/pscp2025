"""a"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())

CAPS = 0
SUMC = 0

for _ in range(d):
    _ += 0 # FUCK YOU PEP8
    if 0 < b <= CAPS:
        SUMC += c
        CAPS -= b
    else:
        SUMC += a
    CAPS += 1

print(SUMC)
