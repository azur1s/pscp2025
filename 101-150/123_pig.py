"""a"""

n = int(input())
ws = input().split()
added = []
SUMW = 0

if n == 1:
    print(f"{max(*ws)}")
else:
    for i in range(n):
        w1 = int(ws[i * 2])
        w2 = int(ws[i * 2 + 1])
        chosenw = w1 if w1 > w2 else w2
        added.append(str(chosenw))
        SUMW += chosenw

    print(f"{' + '.join(added)} = {SUMW}")
