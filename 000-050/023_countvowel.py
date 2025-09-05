"""a"""
n = int(input())
i = 0
for a in range(n):
    # fuck you pep8 fym '_' is not unused like no shit bro
    a = a + 1
    s = input()
    if s.lower() in "aeiou":
        i += 1

print(i)
