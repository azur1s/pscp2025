"""a"""
F = -1 # First number in the current range
L = -1 # Last number in the current range
OUT = ""
while True:
    n = int(input())
    if n == -1:
        # Print the last range before breaking
        if F != -1: # Only if we have seen at least one number
            if F == L: # Single number case
                OUT += f"{F}"
            else: # Range case
                OUT += f"{F}-{L}"
        break

    if F == -1: # First number case
        F = n

    # If the last number + 1 is not equal to the current number, then we have a
    # break in the sequence
    if L + 1 != n and L != -1:
        if F == L: # Single number case
            OUT += f"{F}, "
        else: # Range case
            OUT += f"{F}-{L}, "
        F = n # Start a new range

    L = n # Update the last number
print(OUT)
