"""a"""
n = int(input())
best = (0, 0) # amt, score
for j in range(n):
    j = j + 1 # shut up pep8
    x = int(input())
    if x > best[1]:
        best = (1, x)
    elif x == best[1]:
        best = (best[0] + 1, x)

print(best[1])
print(best[0])
