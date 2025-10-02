"""a"""
import json
xs = json.loads(input())
ys = json.loads(input())
p = int(input())

xs = list(filter(lambda x: x <= p, xs))
ys = list(filter(lambda y: y <= p, ys))

freq = {}
C = 0

for x in xs:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1

for y in ys:
    C += freq.get(p - y, 0)

print(C)
