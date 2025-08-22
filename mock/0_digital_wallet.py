"""a"""
name = input()
isthai = input()
ishome = input()
age = float(input())
income = float(input()) # per year
deposit = float(input())

isthai = True if isthai == "True" or isthai == "Yes" else False
ishome = True if ishome == "True" or ishome == "Yes" else False

OK = False

if isthai and ishome and\
    age >= 16 and\
    income <= 840_000 and\
    deposit <= 500_000:
    OK = True

if OK:
    print(f"Congratulations! {name} is qualified to receive a digital wallet",
        "amount of 10,000 baht, sponsored by all taxpayers in Thailand.",
        sep=" "
    )
else:
    print(f"Unfortunately, {name} is not qualified.")
