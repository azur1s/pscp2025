"""a"""
import math

xs = [input() for _ in range(5)]

# *****  *   *  *   *
#     *   * *   *   *
# *****    *    *****
#     *   * *       *
# *****  *   *      *

a = list(map(lambda line: line[:5],   xs))
o = list(map(lambda line: line[7:12], xs))
b = list(map(lambda line: line[14:],  xs))

nmap = [
    ["*****",
     "*   *",
     "*   *",
     "*   *",
     "*****"],

    ["    *",
     "    *",
     "    *",
     "    *",
     "    *"],

    ["*****",
     "    *",
     "*****",
     "*    ",
     "*****"],

    ["*****",
     "    *",
     "*****",
     "    *",
     "*****"],

    ["*   *",
     "*   *",
     "*****",
     "    *",
     "    *"],

    ["*****",
     "*    ",
     "*****",
     "    *",
     "*****"],

    ["*****",
     "*    ",
     "*****",
     "*   *",
     "*****"],

    ["*****",
     "    *",
     "    *",
     "    *",
     "    *"],

    ["*****",
     "*   *",
     "*****",
     "*   *",
     "*****"],

    ["*****",
     "*   *",
     "*****",
     "    *",
     "*****"],
]

opmap = [
    ["  *  ",
     "  *  ",
     "*****",
     "  *  ",
     "  *  "],
    ["     ",
     "     ",
     "*****",
     "     ",
     "     "],
    ["*   *",
     " * * ",
     "  *  ",
     " * * ",
     "*   *"],
    ["  *  ",
     "     ",
     "*****",
     "     ",
     "  *  "],
]

# print(a)
# print(nmap.index(a))
# print(o)
# print(opmap.index(o))
# print(b)
# print(nmap.index(b))

match opmap.index(o):
    case 0:
        print(nmap.index(a) + nmap.index(b))
    case 1:
        print(nmap.index(a) - nmap.index(b))
    case 2:
        print(nmap.index(a) * nmap.index(b))
    case 3:
        if nmap.index(b) == 0:
            print("Error")
        else:
            print(math.ceil(nmap.index(a) / nmap.index(b)))
