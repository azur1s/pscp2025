"""a"""
text = input()

common = [
    "what", "when", "why", "which", "this", "there", "where",
    "the", "is", "am", "are", "you", "we", "they", "he", "she", "it",
]

def cshift(ch, s):
    """a"""
    if 'a' <= ch <= 'z':
        return chr((ord(ch) - ord('a') + s) % 26 + ord('a'))
    if 'A' <= ch <= 'Z':
        return chr((ord(ch) - ord('A') + s) % 26 + ord('A'))
    return ch

SHIFT = 0
SHIFTED = text

while True:
    if any(c in SHIFTED.split() for c in common):
        print(SHIFTED)
        break
    SHIFT += 1
    SHIFTED = ''.join(cshift(ch, SHIFT) for ch in text)
    if SHIFT > 25:
        print("unreachable?")
