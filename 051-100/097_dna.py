"""a"""
DNA1 = input()
DNA2 = input()

if not set(DNA1).issubset(set("ACGT")) or not set(DNA2).issubset(set("ACGT")):
    print("Error")
else:
    L1, L2 = len(DNA1), len(DNA2)
    S1, S2 = set(), set()
    # "example" -> "e", "x", ... "e", "ex", "xa", ... "le", "exa", "xam" ...
    for i in range(L1):
        for j in range(i + 1, L1 + 1):
            S1.add(DNA1[i:j])

    for i in range(L2):
        for j in range(i + 1, L2 + 1):
            S2.add(DNA2[i:j])

    S = S1.intersection(S2)
    # if S is empty, print "None"
    if not S:
        print("None")
    else:
        S = sorted(S, key=len, reverse=True)
        print(S[0])
