"""a"""
n = int(input())

def f(total, income, threshold, amount):
    """a"""
    # e.g. 600000 -> (600000, 500000, 15%)
    if income > threshold:
        # (600000 - threshold) * 15%, threshold
        # 100000 * 15%, 500000
        return total + ((income - threshold) * amount), threshold
    return 0, income

acc, n = f(0,   n, 4_000_000, 0.35)
acc, n = f(acc, n, 2_000_000, 0.30)
acc, n = f(acc, n, 1_000_000, 0.25)
acc, n = f(acc, n, 750_000,   0.20)
acc, n = f(acc, n, 500_000,   0.15)
acc, n = f(acc, n, 300_000,   0.10)
acc, n = f(acc, n, 150_000,   0.05)
n = n + 1

print(int(acc))
