"""A"""
A = 0
B = 0

for x in range(10):
    x = x + 1
    A += int(input())
for x in range(10):
    x = x + 1
    B += int(input())

if A == B:
    print("AB")
elif A > B:
    print("B")
else:
    print("A")
