# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 11:54:01 2024

@author: Nguyễn Phú Quỳnh Như
"""
a = int(input("nhập số nguyên a"))
b = int(input("nhập số nguyên b"))
c = int(input("nhập số nguyên c"))
d = int(input("nhập số nguyên d"))
minvalue = a
if b < minvalue:
    minvalue = b
if c < minvalue:
    minvalue = c
if d < minvalue:
    minvalue = d
print("kết quả nhỏ nhất", minvalue)