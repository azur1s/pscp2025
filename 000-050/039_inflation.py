"""a"""
def main():
    """a"""
    c = int(float(input()) * 100)
    y = int(input())
    percent = 381
    for _ in range(y):
        c += (c * percent) // 10000
    print(f"{c // 100}.{c % 100:02d}")
main()
