"""a"""
total = float(input())
high = float(input())

total -= high

tenN = total // 10
left = total % 10

if left > 0 and abs(high - left) > 2:
    print("Surprising")
else:
    print("Not surprising")
