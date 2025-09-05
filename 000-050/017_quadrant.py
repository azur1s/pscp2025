"""a"""
x = int(input())
y = int(input())

if x > 0 and y > 0:
    print("Q1")
# elif x < 0 and y > 0:
elif x < 0 < y:
    print("Q2")
elif x < 0 and y < 0:
    print("Q3")
# elif x > 0 and y < 0:
elif x > 0 > y:
    print("Q4")
elif not y and x:
    print("X")
elif not x and y:
    print("Y")
else:
    print("O")
