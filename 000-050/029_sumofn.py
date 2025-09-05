"""a"""
n = int(input())
i = 0
while True:
    x = int(input())
    if x == -1:
        print(i)
        break
    i += x
    if i == n:
        print(i)
        break
