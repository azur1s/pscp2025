"""temperature"""
def k_to_c(k):
    """asd"""
    return k - 273.15

def f_to_c(f):
    """asd"""
    return (f - 32) * 5 / 9

def r_to_c(r):
    """asd"""
    return (r * 5 / 9) - 273.15

def c_to_k(c):
    """asd"""
    return c + 273.15

def c_to_f(c):
    """asd"""
    return c * 9 / 5 + 32

def c_to_r(c):
    """asd"""
    return (c + 273.15) * 9 / 5

temp = float(input())
from_t = input()
to_t = input()

RESULT = 0

match from_t:
    case 'C':
        RESULT = temp
    case 'K':
        RESULT = k_to_c(temp)
    case 'F':
        RESULT = f_to_c(temp)
    case 'R':
        RESULT = r_to_c(temp)

match to_t:
    case 'C':
        print(f"{RESULT:.2f}")
    case 'K':
        print(f"{c_to_k(RESULT):.2f}")
    case 'F':
        print(f"{c_to_f(RESULT):.2f}")
    case 'R':
        print(f"{c_to_r(RESULT):.2f}")
