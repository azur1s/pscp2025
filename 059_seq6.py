"""a"""
print("\n".join([" ".join([str(j + 1)
                           for j in range(i + 1)])
                 for i in range(int(input()))]))
