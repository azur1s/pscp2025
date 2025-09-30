"""a"""
a = float(input())
b = float(input())
vote2 = a - b
highest = min(b, vote2)
vote = vote2 - highest
if b - 2 > vote:
    print("Surprising")
else:
    print("Not surprising")
