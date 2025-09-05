"""A"""
s = input().upper()
A = ""
match s[0]:
    case 'A':
        A += "Ace of "
        s = s[1:]
    case 'Q':
        A += "Queen of "
        s = s[1:]
    case 'K':
        A += "King of "
        s = s[1:]
    case 'J':
        A += "Jack of "
        s = s[1:]
    case _:
        A += s[0]
        s = s[1:]
        if s[0].isdigit():
            A += s[0]
            s = s[1:]
        A += " of "

match s:
    case 'C':
        A += "Clubs"
    case 'D':
        A += "Diamonds"
    case 'H':
        A += "Hearts"
    case 'S':
        A += "Spades"
    case _:
        raise LookupError

print(A)
