"""a"""
def f(g, i):
    """a"""
    if not i:
        return g
    x = int(input())
    if not x % 2:
        g = x
    return f(g, i - 1)

print(f(0, 8))
