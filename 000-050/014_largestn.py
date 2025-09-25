'''Largest Number'''
def fuck_you(x, y, z):
    """FUCK YOUUUU"""
    case1 = int(str(x) + str(y) + str(z))
    case2 = int(str(x) + str(z) + str(y))
    case3 = int(str(y) + str(x) + str(z))
    case4 = int(str(y) + str(z) + str(x))
    case5 = int(str(z) + str(y) + str(x))
    case6 = int(str(z) + str(x) + str(y))

    casemak = case1
    if casemak < case2:
        casemak = case2
    if casemak < case3:
        casemak = case3
    if casemak < case4:
        casemak = case4
    if casemak < case5:
        casemak = case5
    if casemak < case6:
        casemak = case6
    return casemak

def main():
    '''main'''
    a = int(input())
    b = int(input())
    c = int(input())

    if a >= b and a >= c:
        x = a
        if b >= c:
            y = b
            z = c
        else:
            y = c
            z = b
    elif b >= a and b >= c:
        x = b
        if a >= c:
            y = a
            z = c
        else:
            y = c
            z = a
    else:
        x = c
        if a >= b:
            y = a
            z = b
        else:
            y = b
            z = a

    print(fuck_you(x, y, z))

main()
