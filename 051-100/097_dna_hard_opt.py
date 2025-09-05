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
    # build a table to store the longest common substring
    TABLE = [[0] * (L2 + 1) for _ in range(L1 + 1)]
    MAX_LEN = 0
    END_POS = 0

    # example "AAACTGCT" & "ACACTGCA" = "ACTGC"
    #     0 1 2 3 4 5 6 7
    #     A A A C T G C T
    #         ┌────────┐
    # 0 A 1 1 1 0 0 0 0 0   * iterate over each character pair
    # 1 C 0 0 0 2 0 0 1 0
    # 2┌A 1 1[1]0 0 0 0 0 ┐ * if both chars match, increment the length
    # 3│C 0 0 0[2]0 0 1 0 │   from the previous position (i - 1, j - 1)
    # 4│T 0 0 0 0[3]0 0 1 │   and then update the maximum length and end
    # 5│G 0 0 0 0 0[4]0 0 │   position to be at the current position (i, j)
    # 6└C 0 0 0 1 0 0[5]0 ┘
    # 7 A 1 1 1 0 0 0 0 0   * in this case, max length is 5 and end position
    #                         is at index 7 (1-based), which means
    #                         the longest is [7 - 5:7] = "ACTGC"

    # iter over each character in both DNA sequences
    for i in range(1, L1 + 1):
        for j in range(1, L2 + 1):
            dna1 = DNA1[i - 1]
            dna2 = DNA2[j - 1]
            if dna1 == dna2: # if characters match
                # increment the length of the common substring
                TABLE[i][j] = TABLE[i - 1][j - 1] + 1
                # if this is the longest found so far
                if TABLE[i][j] > MAX_LEN:
                    # update the maximum length and end position
                    MAX_LEN = TABLE[i][j]
                    END_POS = i # position in DNA1

    longest = DNA1[END_POS - MAX_LEN:END_POS]
    if not MAX_LEN:
        print("None")
    else:
        print(longest)
