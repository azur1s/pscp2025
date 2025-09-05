"""a"""
w = int(input())
d = input()
text = input()

match d:
    case "left":
        print(text.ljust(w, ' '))
    case "center":
        if len(text) % 2 and not w % 2:
            left_padding = (w - len(text)) // 2 + 1
            right_padding = w - len(text) - left_padding
            print(' ' * left_padding + text + ' ' * right_padding)
        else:
            print(text.center(w, ' '))
    case "right":
        print(text.rjust(w, ' '))
