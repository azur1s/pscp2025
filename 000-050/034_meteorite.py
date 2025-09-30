"""a"""
import math
a = float(input())
b = int(input())
c = float(input())
if a < c:
    print(0)
else:
    k = math.floor(math.log(a / c, b)) + 1
    count = (b ** k - 1) // (b - 1)
    print(count)
