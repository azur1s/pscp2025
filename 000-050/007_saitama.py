"""a"""
import math
W = int(input()) # วิดพื้น
S = int(input()) # ซิทอัพ
L = int(input()) # ลุกนั่ง
R = int(input()) # วิ่ง

# days
DW = W / int(input()) # วันวิดพื้น
DS = S / int(input()) # วันซิทอัพ
DR = R / int(input()) # วันวิ่ง
DL = L / int(input()) # วันลุกนั่ง

def m(a, b, c, d):
    """idc"""
    if a >= b and a >= c and a >= d:
        return a
    if b >= a and b >= c and b >= d:
        return b
    if c >= a and c >= b and c >= d:
        return c
    return d

print(int(math.ceil(m(DW, DS, DR, DL))))
