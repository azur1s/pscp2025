"""a"""
N = str(int(input()))
S = ""
OK = False
if len(N) == 2 or N == "5":
    if N[-1] == "0":
        S += "Horizontal Major Interstate\n"
    else:
        S += "Vertical Major Interstate\n"

    S += f"I-{int(N)}"

if len(N) == 3:
    if not int(N[0]) % 2:
        S += "Even Minor Interstate\n"
    else:
        S += "Odd Minor Interstate\n"

    S += f"I-{int(N[1:])}"

if (2 <= len(N) <= 3 if N != "5" else True)\
and (not int(N[-1]) or int(N[-1]) == 5)\
and (int(N) % 100 if len(N) == 3 else True):
    OK = True

if not OK:
    print("Others")
else:
    print(S)
