"""a"""
p, q, r = int(input()), int(input()), int(input())
A = [[int(input()) for _ in range(q)] for _ in range(p)]
B = [[int(input()) for _ in range(r)] for _ in range(q)]
for i in range(p):
    print(*[sum(A[i][k] * B[k][j] for k in range(q)) for j in range(r)])
