"""a""";import re;print('\n'.join(('no','yes')[bool(re.fullmatch(r'(bakka|ba(?!ka)|ka|ta)+',input()))]for _ in range(int(input()))))
