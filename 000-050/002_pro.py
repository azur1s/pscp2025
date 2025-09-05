"""asdasdasdasd"""
pro_x  = int(input())
pro_y  = int(input())
price  = int(input())
amount = int(input())

reduced = (amount // pro_x) * pro_y * price
normal = (amount % pro_x) * price

print(reduced + normal)
