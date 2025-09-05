"""a"""

def fib(x):
    """a"""
    return fib(x - 1) + fib(x - 2) if x > 1 else x

print(fib(int(input())))
