"""a""" # holy shit
x, y = map(int, input().split(" x "))
grid = [input().split() for _ in range(y)]
Enu = enumerate
xs = [                str
                    (    len(
                   list      #
                ( filter(     #
                lambda x:     #
                x == "*",
                [grid[i+a
                ] [j + b]
                for a  in
                range(-1,
                2) for b
                in range(
                -1, 2) if
          0 <=  i + a < y  and
        0 <= j + b < x] ) )) )if
       cell  == "0" else cell for
       (i, row) in enumerate(grid)
        for(j, cell)  in Enu(row)
]
list(print(" ".join(xs[i * x:(i + 1) * x])) for i in range(y))
