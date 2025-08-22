"""a"""
d = int(input())
d = d + 1
a = input()
b = input()

W = 0
for (a, b) in zip(a, b):
    if int(a) + int(b) != 9:
        W += 1

if not W:
    print("YES")
else:
    print("NO " + str(W))
