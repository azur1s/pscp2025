"""a"""
import math

x1, y1, r1 = (int(input()), int(input()), int(input()))
x2, y2, r2 = (int(input()), int(input()), int(input()))

d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
if d >= r1 + r2:
    print("no overlapping")
else:
    print("overlapping")

# x_overlap = abs(x1 - x2) < (r1 + r2)
# y_overlap = abs(y1 - y2) < (r1 + r2)
# if x_overlap and y_overlap:
#     print("overlapping")
# else:
#     print("no overlapping")
