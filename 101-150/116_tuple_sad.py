"""a"""
tp = tuple(input().split())
x = input()

count = tp.count(x)
index = tp.index(x)

for i in range(count):
    i = i + 1
    for j in range(count):
        if j == count - 1:
            print(index)
        else:
            print(index, end=" ")
