"""a"""
# Time  : O(len(xs) * n)
# Space : O(1) yay!
xs = list(map(int, input()[1:-1].split(',')))
n = int(input()) # Amount of numbers we want
s = int(input()) # How many numbers to skip

def once(shift):
    x = 0
    i = 0
    while i < n: # O(n)
        index = (i * s) + shift
        x += xs[index % len(xs)]
        i += 1
    return x

MAX = 0
for i in range(len(xs)): # O(len(xs)) + O(n) at each iterations
    MAX = max(MAX, once(i))
print(MAX)
