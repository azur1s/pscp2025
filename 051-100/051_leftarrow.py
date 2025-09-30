"""a"""
w = int(input())
h = int(input())

for i in range(h // 2, 0, -1):
    print(f"{' ' * i}{'*' * w}")
print(f"{'*' * w}")
for i in range(h // 2):
    print(f"{' ' * (i + 1)}{'*' * w}")
