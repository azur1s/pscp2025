"""a"""
x = input()
xs = list(filter(lambda x: not (x % 3) or not (x % 5),
            map(int, reversed(x.split()))))
print("\n".join(map(str, xs)) if xs else "Nope")
