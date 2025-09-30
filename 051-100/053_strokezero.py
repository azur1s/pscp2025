"""a"""
n = int(input())

for i in range(1, n + 1):
    if i == 1:
        print("0")
    elif i == n:
        print(" ".join(["0"] * n))
    else:
        row = ["0"] + (["1"] * (i - 2)) + ["0"]
        print(" ".join(row))
