"""a"""
xs = list(range(1, int(input()) + 1))
# read "for every number x in xs...
ans = [x for x in xs if
       # ..check if x is divisible by any perfect square > 1"
       all(x % (i * i) for i in range(2, int(x**0.5) + 1))]
print(len(ans))
