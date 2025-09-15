"""a"""
# Time  : O(len(xs) * (len(xs) // gcd(s, len(xs))))
# Space : O(1) yay!
import math
xs = list(map(int, input()[1:-1].split(',')))
n = int(input()) # Amount of numbers we want
s = int(input()) # How many numbers to skip

"""
Since at some point the `(i * s) + shift % len(xs)` will loop around (refer to
199_brng_v1.py), we can calculate the sum up until those point, and then
multiply it until it reaches `n` (by calculating full cycles and remainder since
it probably won't be divisible by `n`) so that the O notation doesn't
depends on `n`

The reason 199_brng_v1.py with `while i < n` doesn't work because if `n` were
to be very large (and I know it will), we will have to iterate `n` loops and
it will be pointless when we are indexing the same number

Look at the pattern:
(1) [ 1 2 3 ], skip = 2, start i = 0
    0 .     |
    1     . | 2
    2 .     <- repeat
Indexed xs will be 1, 3, 1, 3, 1, 3...

(2) [ 1 2 3 4 5 ], skip = 5, start i = 0
    0 .         |
    1     .     |
    2         . | 5
    3   .       |
    4       .   |
    5 .         <- repeat
Indexed xs will be 1, 3, 5, 2, 4, 1, 3, 5, 2, 4, 1, 3, 5...

(3) [ 1 2 3 4 5 6 7 ], skip = 3, start i = 1
    0   .           |
    1         .     |
    2 .             |
    3       .       | 7
    4             . |
    5     .         |
    6           .   |
    7   .           <- repeat
2, 5, 1, 4, 7, 3, 6... you get the point

From above, the period will be the greatest common divisor of `s` and `len(xs)`,
so we can just multiply until `n` and get the rest via remainder
(1) -> cycle is 2 (gcd(2, 3) = 2)
    n = 10 -> sum * (10 // 2) + remainder sum * (10 % 2)
(2) -> cycle is 5 (gcd(5, 5) = 5)
    n = 8  -> sum * (8 // 5) + remainder sum * (8 % 5)
           -> sum * 1 + remainder sum * 3
etc.

So we:
1) Compute the sum for one cycle
2) Multiply number until we reach `n` iterations
3) Do the remaining iterations
gg

Now the O notation doesn't depends on `n`! wow!!!
for 199_brng_v1.py, see:
    https://github.com/azur1s/pscp2025/tree/main/151-200/199_brng_v1.py
"""

MAX = 0
for shift in range(len(xs)):
    # Calculate sum for one cycle
    cycle = len(xs) // math.gcd(s, len(xs))
    CYCLE_SUM = 0
    for i in range(cycle):
        CYCLE_SUM += xs[(i * s + shift) % len(xs)]
    # Then calculate how much full cycle (and remainder) we need until we reach
    # the amount of numbers we want (`n`)
    needed_cycles = n // cycle
    remainder_cycles = n % cycle
    REMAINDER_SUM = 0
    for i in range(remainder_cycles):
        REMAINDER_SUM += xs[(i * s + shift) % len(xs)]
    # Compare
    MAX = max(MAX, CYCLE_SUM * needed_cycles + REMAINDER_SUM)
print(MAX)
