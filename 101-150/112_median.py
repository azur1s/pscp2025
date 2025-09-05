"""a"""
xs = sorted(map(float, input().split(", ")))
if len(xs) % 2 == 1:
    print(f"{xs[len(xs) // 2]:.2f}")
else:
    n1 = xs[len(xs) // 2 - 1]
    n2 = xs[len(xs) // 2]
    print(f"{(n1 + n2) / 2:.2f}")
