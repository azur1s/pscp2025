"""a"""
RA = int(input())
RB = int(input())
AB = input()

def elo(a, b):
    """idc"""
    if AB == "A":
        return 1 / (1 + 10 ** ((b - a) / 400))
    return 1 / (1 + 10 ** ((a - b) / 400))

print(f"{elo(RA, RB):.2f}")
