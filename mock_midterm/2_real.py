"""a"""
def once():
    a = (True if input() == "on" else False)
    b = (True if input() == "on" else False)
    c = (True if input() == "on" else False)
    d = (True if input() == "on" else False)
    e = (True if input() == "on" else False)
    f = (True if input() == "on" else False)
    g = (True if input() == "on" else False)
    dp = (True if input() == "on" else False)

    X = -1
    if a & b & c & d & e & f &     (not g): X = 0
    elif b & c & (not (a | d | e | f | g)): X = 1
    elif a & b & d & e & g & (not (c | f)): X = 2
    elif a & b & c & d & g & (not (e | f)): X = 3
    elif b & c & f & g & (not (a | d | e)): X = 4
    elif a & c & d & f & g & (not (b | e)): X = 5
    elif a & c & d & e & f & g &   (not b): X = 6
    elif a & b & c & (not (d | e | f | g)): X = 7
    elif a & b & c & d & e & f & g:         X = 8
    elif a & b & c & d & f & g &   (not e): X = 9
    return X, dp

def format_dp(dp):
    return "." if dp else ""

A, dp0 = once()
B, dp1 = once()
C, dp2 = once()

if A == -1 or B == -1 or C == -1:
    print("Error")
else:
    try:
        F = float(f"{A}{format_dp(dp0)}{B}{format_dp(dp1)}{C}{format_dp(dp2)}")
        print(f"{F:.2f}")
    except:
        print("Error")