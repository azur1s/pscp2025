"""a"""
shift = int(input())
text = input()

result = []
for char in text:
    if 'a' <= char <= 'z':
        new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
    elif 'A' <= char <= 'Z':
        new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
    else:
        new_char = char
    result.append(new_char)
print("".join(result))
