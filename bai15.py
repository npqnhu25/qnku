# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 11:47:20 2024

@author: Nguyễn Phú Quỳnh Như
"""

a = int(input("nhập a là"))
b = int(input("nhập b là"))
A = ((a + b) / (pow(a,(1 / 3)) + pow(b,(1 / 3)))) - pow(a * b,(1 / 3))
B = (pow(a,(1 / 3)) - pow(b,(1 / 3))) ** 2
print("kết quả là", A / B)