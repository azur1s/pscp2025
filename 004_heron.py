"""a"""
import math

A = float(input())
B = float(input())
C = float(input())

S = (A + B + C) / 2
area = math.sqrt(S * (S - A) * (S - B) * (S - C))
print(f"{area:.3f}")
