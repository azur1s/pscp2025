"""a"""
xs = []
while True:
    x = input()
    if x == "NULL":
        break
    xs.append(x)

print('\n'.join(list(reversed(xs))))
