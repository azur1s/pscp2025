"""doc"""
def main():
    """main"""
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())

    donut = 0
    price = 0

    while donut < d:
        price += 1
        donut += 1
        if not price % b:
            donut += c

    print(price * a, donut)

main()
