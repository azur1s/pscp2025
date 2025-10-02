"""a"""
s = [input().strip() for _ in range(5)]
sp = max(len(line) for line in s)

print("*" * (sp + 4))
for i in range(5):
    print("* " + s[i].ljust(sp, ' ') + " *")
print("*" * (sp + 4))
