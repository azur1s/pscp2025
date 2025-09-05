"""a"""
n_exact = input()
n_l2    = input()
n_f3a   = input()
n_f3b   = input()
n_l3a   = input()
n_l3b   = input()
x       = input()

R = 0

if x == n_exact:
    R += 6_000_000

if x[-2:] == n_l2:
    R += 2_000

# if x[:3] == n_f3a or x[:3] == n_f3b:
if x[:3] == n_f3a:
    R += 4_000
if x[:3] == n_f3b:
    R += 4_000

# if x[-3:] == n_l3a or x[-3:] == n_l3b:
if x[-3:] == n_l3a:
    R += 4_000
if x[-3:] == n_l3b:
    R += 4_000

if int(x) == (int(n_exact) - 1) % 1_000_000\
or int(x) == (int(n_exact) + 1) % 1_000_000:
    R += 100_000

print(R)
