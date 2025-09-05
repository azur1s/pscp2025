"""a"""
start = input()
amt = int(input())

pat = ["Red", "Green", "Blue"]
if start == "G":
    pat = ["Green", "Blue", "Red"]
elif start == "B":
    pat = ["Blue", "Red", "Green"]

pats = pat * int(amt // 3) + pat[:amt % 3]

print(" ".join(pats))
