"""a"""
amt = int(input())
years = [input() for _ in range(amt)]

for year in years:
    X = 0
    if year.startswith("B.E. "):
        X = int(year[5:]) - 543
    else:
        X = int(year[5:])
    if X <= 0:
        print("ERROR")
    else:
        print(X // 100 + (1 if X % 100 > 0 else 0))
