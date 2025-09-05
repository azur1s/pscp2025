"""a"""
n = int(input())
print("\n".join(
    [" ".join(
            [str(j + 1).zfill(2) for j in range(i + 1)]
        ).rjust(3 * n - 1, ' ')
    for i in range(n)]
))
