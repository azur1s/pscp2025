"""a"""
n = int(input())

def line(l):
    """01 .. 0n"""
    return " ".join([str(j + 1).zfill(2) for j in range(l)])

def line_rev(l):
    """0n-1 .. 01"""
    return " ".join([str(j + 1).zfill(2) for j in reversed(range(l))])

print("\n".join(
    [line(i + 1).rjust(3 * n - 1, ' ') + ' ' + line_rev(i) for i in range(n)]
))
