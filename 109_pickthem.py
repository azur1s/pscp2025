"""a"""
import json
xs = list(filter(lambda x: not (x % 2), json.loads(input())))
print("\n".join(map(str, xs)) if len(xs) > 0 else "Nope")
