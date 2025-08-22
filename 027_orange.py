"""a"""
x = int(input())
y = int(input())
a = [i * i for i in range(1, x + 1)]
B = 0
while y > 0:
    a[0] -= 1
    if not a[0]:
        B += 1
        a = a[1:]
    y -= 1
print(len(a))
