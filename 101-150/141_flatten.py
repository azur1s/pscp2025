"""a"""
import json
xs = json.loads(input())
def flatten(ys):
    """a"""
    return [z for y in ys for z in flatten(y)]\
        if isinstance(ys, list)\
        else [ys]
print(sorted(flatten(xs), reverse=True))
