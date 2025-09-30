"""a"""
xs = [int(input()) for _ in range(int(input()))]
print(max({x: xs.count(x) for x in xs}.values()))
