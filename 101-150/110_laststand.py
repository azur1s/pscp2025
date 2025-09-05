"""a"""; import json
print(*list(map(lambda x: str(x)[-1], json.loads(input()))), sep="\n")
