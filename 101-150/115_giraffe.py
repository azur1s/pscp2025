"""a"""
n = int(input())
gs = [int(input()) for _ in range(n)]

print(len(list(
      filter(lambda w: w[1] > w[0] and w[1] > w[2],
           map(lambda x: (
               # Sliding window, if out of bounds, use 0
               # 0 | 1 2 3 | 0
                gs[x[0] - 1] if x[0] else 0,
                x[1],
                gs[x[0] + 1] if x[0] != len(gs) - 1 else 0),
               enumerate(gs))))))
