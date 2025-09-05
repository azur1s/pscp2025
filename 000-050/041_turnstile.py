"""a"""
LOCKED = True
AMT = 0
while True:
    x = input()
    if x == "END":
        break

    if x == "C":
        LOCKED = False
    elif x == "P" and not LOCKED:
        AMT += 1
        LOCKED = True
    elif x == "P" and LOCKED:
        pass

print(AMT)
