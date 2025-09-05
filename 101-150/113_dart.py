"""a"""
n = int(input())
xs = [input().split() for _ in range(n)]
SCORE = 0
for x in xs:
    x, y = map(int, x)
    if x ** 2 + y ** 2 <= 4:
        SCORE += 5
    elif x ** 2 + y ** 2 <= 16:
        SCORE += 4
    elif x ** 2 + y ** 2 <= 36:
        SCORE += 3
    elif x ** 2 + y ** 2 <= 64:
        SCORE += 2
    elif x ** 2 + y ** 2 <= 100:
        SCORE += 1

print(SCORE)
