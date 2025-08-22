"""a"""
s = input()
groups = []

for ch in s: # for char in string
    if not groups: # if list is empty
        groups.append([1, ch]) # append (amount, char)

    elif ch == groups[-1][1]: # if char == previous char
        groups[-1][0] += 1 # previous char += 1

    else: # else if the char doesn't match
        groups.append([1, ch]) # append (amount, char)

# for (amount, char) in groups, str(amount) + char
print("".join([str(x[0]) + x[1] for x in groups]))
