"""a"""
x = int(input())
print("PONG" if not x % 3 or str(x)[-1] == '3' else x)
