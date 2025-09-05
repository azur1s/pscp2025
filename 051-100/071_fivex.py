"""a"""
n = int(input())
print("".join("X" if not (i + 1) % 5 else "*" for i in range(n)))
