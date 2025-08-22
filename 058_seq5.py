"""a"""
xs = [str(i + 1) for i in reversed(range(int(input())))]
i = 0
while i < len(xs):
    print(" ".join(xs[i:i + 7]))
    i += 7
