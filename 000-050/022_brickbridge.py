"""a"""
a = int(input())
b = int(input())
goal = int(input())

big_used = min(b, goal // 5)
length_left = goal - (big_used * 5)

if length_left <= a:
    print(length_left)
else:
    print("-1")
