"""a"""
n = input()
#               domestic       international
# 021234567  -> 0  2123 4567 | +66  2123 4567
# 0811234567 -> 08 1123 4567 | +668 1123 4567
if input() == "Domestic":
    last4 = n[-4:]
    mid4 = n[-8:-4]
    start = n[0] if len(n) == 9 else n[0:2]
    print(f"{start} {mid4} {last4}")
else:
    last4 = n[-4:]
    mid4 = n[-8:-4]
    start = n[1] if len(n) == 10 else ""
    print(f"+66{start} {mid4} {last4}")
