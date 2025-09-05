"""a"""
m = int(input())
d = int(input())

season = ["winter", "spring", "summer", "fall"]
i = m // 3 # 1-2, 3-5, 6-8, 9-11, 12
if not m % 3 and d < 21:
    i -= 1

if i > 3:
    i = 0

print(f"{season[i]}")
