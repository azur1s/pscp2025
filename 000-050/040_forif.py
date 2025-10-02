"""a"""
A, B, C = 1, 0, 0
for x in input():
    if x == "A":
        A, B = B, A
    elif x == "B":
        B, C = C, B
    elif x == "C":
        A, C = C, A

if A == 1:
    print("1")
elif B == 1:
    print("2")
else:
    print("3")
