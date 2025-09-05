"""a"""
n = int(input())
print("\n".join([" ".join([str(j + 1)
                           for j in range(i + 1)])
                 for i in range(n)]))
print("\n".join([" ".join([str(j + 1)
                           for j in range(i + 1)])
                 for i in reversed(range(n - 1))]))
