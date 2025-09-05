"""a"""

dim = input()
x = int(dim[:2])
y = int(dim[-2:])
grid = [input() for _ in range(y)]

# 23 x 20
# grid = [
#     "0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 * * 0 0 0 0 *",
#     "0 0 0 0 0 0 * 0 0 0 0 0 * 0 0 * 0 * * 0 0 0 0",
#     "* 0 0 0 * * * * * 0 * * 0 0 * 0 * 0 0 0 0 * *",
#     "0 0 0 0 * * 0 0 0 0 0 0 0 * * 0 0 0 * 0 * * 0",
#     "0 * * 0 0 0 0 * 0 * 0 0 * * * * 0 0 0 0 0 * *",
#     "0 0 0 * * 0 0 0 0 0 * 0 0 0 * 0 0 * 0 0 0 0 0",
#     "* * 0 0 0 0 0 0 0 * 0 0 0 * 0 0 0 0 * 0 0 0 0",
#     "0 0 0 0 0 * 0 0 0 0 * 0 0 0 0 0 0 0 0 * 0 0 0",
#     "0 0 0 * 0 * 0 * 0 0 * 0 0 0 0 0 0 0 * 0 * 0 0",
#     "0 * 0 0 0 0 0 * 0 * 0 * 0 * 0 * 0 0 0 0 0 0 0",
#     "0 0 0 * 0 0 0 0 0 0 0 0 0 0 * * 0 * 0 0 0 0 *",
#     "0 * 0 0 0 0 0 0 0 0 0 * 0 0 0 0 0 0 0 * 0 0 0",
#     "0 0 0 0 0 0 0 0 * 0 * * 0 0 0 0 0 * * 0 0 0 0",
#     "0 0 0 0 0 0 * 0 0 0 0 * 0 0 0 0 * 0 0 0 0 0 0",
#     "* * 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 * 0 * 0 0 *",
#     "0 * * * 0 0 * 0 0 0 0 0 0 * 0 0 * * * * 0 0 0",
#     "* 0 0 0 * 0 * 0 0 0 0 * 0 0 0 * * 0 0 * 0 0 0",
#     "0 * 0 0 0 * 0 0 * 0 0 0 0 0 * 0 0 0 0 0 0 0 0",
#     "* 0 * 0 0 0 0 0 * 0 0 0 0 0 0 0 * 0 0 * 0 0 0",
#     "* 0 0 0 0 0 0 0 0 0 0 * 0 0 0 * 0 0 0 0 0 * 0",
# ]

grid = [line.split() for line in grid]

def get(xs, ix, iy):
    """get"""
    if ix < 0 or iy < 0:
        return ""
    if iy + 1 > len(xs):
        return ""
    if ix + 1 > len(xs[iy]):
        return ""
    return xs[iy][ix]

for (y, line) in enumerate(grid):
    res = []
    for (x, cell) in enumerate(line):
        if cell == "*":
            res.append("*")
        else:
            u  = get(grid, x,     y - 1)
            d  = get(grid, x,     y + 1)
            l  = get(grid, x - 1, y    )
            r  = get(grid, x + 1, y    )
            ul = get(grid, x - 1, y - 1)
            ur = get(grid, x + 1, y - 1)
            dl = get(grid, x - 1, y + 1)
            dr = get(grid, x + 1, y + 1)
            count = len(list(filter(
                lambda x: x == "*",
                [u, d, l, r, ul, ur, dl, dr],
            )))
            res.append(f"{count}")
    print(" ".join(res))
