# RESTRICTED: sort sorted sum {} list append [] join remove dict set pop split tuple

# Check 072_rle.py

"""a"""
s = input()
OUT = "" # output string for final print
LAST_CHAR = "" # last char
LAST_AMT = 0 # last amount

for char in s:
    if not LAST_CHAR: # if last is empty
        LAST_CHAR = char # last is now this char
        LAST_AMT = 1 # init amount

    elif char == LAST_CHAR: # if this char == last char
        LAST_AMT += 1 # increase amount

    else: # if this char != last char
        # append to final string
        OUT += f"{LAST_AMT}{LAST_CHAR}"
        # last is now this char
        LAST_CHAR = char
        # init amount
        LAST_AMT = 1

# Final append
OUT += f"{LAST_AMT}{LAST_CHAR}"

print(OUT)
