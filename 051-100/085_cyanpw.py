"""a"""
n = input()
s = input()
a = input()

if len(n) >= 5 and len(s) >= 5:
    print(n[:2] + s[-1] + a[-1])
else:
    print(n[0] + a + s[-1])
