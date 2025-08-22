# RESTRICTED: sort sorted sum {} list append [] join remove dict set pop split tuple

"""a"""
DNA1 = input()
DNA2 = input()

def valid(dna):
    """a"""
    return all(c in "ACGT" for c in dna)

if not valid(DNA1) or not valid(DNA2):
    print("Error")
else:
    L1, L2 = len(DNA1), len(DNA2)
    CUR = ""
    CUR_LEN = 0

    # "example" -> "e", "x", ... "e", "ex", "xa", ... "le", "exa", "xam" ...
    for i in range(L1):
        for j in range(i + 1, L1 + 1):
            for a in range(L2):
                for b in range(a + 1, L2 + 1):
                    dna1 = DNA1[i:j]
                    dna2 = DNA2[a:b]
                    if not dna1 or not dna2:
                        continue
                    if dna1 == dna2:
                        if len(dna1) > CUR_LEN:
                            CUR = dna1
                            CUR_LEN = len(CUR)

    if not CUR:
        print("None")
    else:
        print(CUR)
