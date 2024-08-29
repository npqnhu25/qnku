# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 12:09:23 2024

@author: Nguyễn Phú Quỳnh Như
"""
a = int(input("nhập a là"))
b = int(input("nhập b là"))
c = int(input("nhập c là"))
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a




N = int(input("nhập số nguyên N"))
danh_sach = list(N)
sap_xep = danh_sach.sort()
sap_xep_danh_sach = "".join(danh_sach)
print(sap_xep_danh_sach)
