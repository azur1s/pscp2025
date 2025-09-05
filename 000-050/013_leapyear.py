"""a"""
year = int(input())

# % 4 == 0 OR if 1800, 1900, 2000 -> % 400 == 0
if (not year % 4 and year % 100) or not year % 400:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
