"""a"""
group = int(input())
for x in range(group):
    x = x + 1 # pep8

    n = int(input())
    points = []

    for x in range(n):
        x = x + 1 # pep8
        x, y = input().split()
        points.append((int(x), int(y)))

    #                         sort by x + y
    #                               |       then by y (descending so `-y`)
    #                               v         v
    points.sort(key=lambda x: (x[0] + x[1], -x[1]))

    print("\n".join(f"{x[0]} {x[1]}" for x in points))
