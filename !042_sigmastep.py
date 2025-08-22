"""a"""
x = int(input()) # start
y = int(input()) # stop
n = int(input()) # step

# x -4 y -30 n -5
# -4 - 9 - 14 - 19 - 24 - 29

if (n < 0 < y) or (n > 0 > y) or (not n):
    print("error")
else:
    accum = x
    step = x
    while True:
        if n > 0 and step + n > y:
            break
        if n < 0 and step + n < y:
            break
        step += n
        accum += step
    print(accum)
