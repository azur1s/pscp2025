"""a"""
a = float(input()) # normal price
b = float(input()) # discount %
c = float(input()) # discount % IF min buy d
d = float(input()) # min buy
e = int(input()) # example buy

X = (max(e - 1, 0) * (a - (a * b * 0.01))) + (a if e >= 1 else 0)
Y0 = e * (a - (a * c * 0.01))
Y = (Y0 if (e * a) >= d else e * a)

if X < Y:
    print(1)
    print(f"{X:.2f}")
else:
    print(2)
    print(f"{Y:.2f}")