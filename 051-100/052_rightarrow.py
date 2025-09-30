"""a"""
w = int(input())
h = int(input())

for i in range((h // 2) + 1):
    print(f"{' ' * i}{'*' * w}")
for i in range(h // 2, 0, -1):
    print(f"{' ' * (i - 1)}{'*' * w}")
