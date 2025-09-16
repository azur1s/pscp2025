"""a"""
dim = input().split(" x ")
x = int(dim[0])
y = int(dim[1])
grid = [input().split() for _ in range(y)]

for (i, row) in enumerate(grid):
    res = []
    for (j, cell) in enumerate(row):
        if cell == "0":
            COUNT = 0
            for a in range(-1, 2):
                for b in range(-1, 2):
                    if  0 <= i + a < y\
                    and 0 <= j + b < x\
                    and grid[i + a][j + b] == "*":
                        COUNT += 1
            res.append(str(COUNT))
        else:
            res.append(cell)
    print(" ".join(res))
