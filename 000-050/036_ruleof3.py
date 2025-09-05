"""a"""
amt = int(input())
xs = []
for i in range(amt):
    i = i + 1 # pep8
    p = float(input())
    g = float(input())
    xs.append((p, g))

xs.sort(key=lambda x: x[0])
ratio = [(p / g, p, g) for p, g in xs]
ratio.sort(key=lambda x: x[0])
print(f"{ratio[0][1]:.2f} {ratio[0][2]:.2f}")
