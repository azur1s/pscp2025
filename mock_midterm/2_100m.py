"""a"""
# time
X = 10000
Y = 10000
Z = 10000
# runner index
XI = 0
YI = 0
ZI = 0

def check(i, t):
    global X, Y, Z, XI, YI, ZI
    if t < X:
        # print(f"> {i} is now first with {t}")
        ZI = YI # 2 -> 3
        Z = Y
        YI = XI # 1 -> 2
        Y = X
        XI = i # i -> 1
        X = t
        # print(">", XI, YI, ZI, sep=" ")
    elif t < Y:
        # print(f"{i} is now second with {t}")
        ZI = YI # 2 -> 3
        Z = Y
        YI = i # i -> 2
        Y = t
        # print(">", XI, YI, ZI, sep=" ")
    elif t < Z:
        # print(f"{i} is now third with {t}")
        ZI = i # i -> 3
        Z = t
        # print(">", XI, YI, ZI, sep=" ")
    else:
        # print(f"{i} ok ({t})")
        pass

a = check(1, float(input()))
b = check(2, float(input()))
c = check(3, float(input()))
d = check(4, float(input()))
e = check(5, float(input()))
f = check(6, float(input()))
g = check(7, float(input()))
h = check(8, float(input()))

print(XI, YI, ZI, sep=" ")
