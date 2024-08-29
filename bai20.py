# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 11:55:32 2024

@author: Nguyễn Phú Quỳnh Như
"""
a = int(input("nhập a"))
b = int(input("nhập b"))
c = int(input("nhập c"))
maxvalue = a
if b > maxvalue:
    maxvalue = b
if c > maxvalue:
    maxvalue = c 
print("kết quả lớn nhất là", maxvalue)


