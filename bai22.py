# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 12:02:41 2024

@author: Nguyễn Phú Quỳnh Như
"""
a = float(input(" nhập số a: "))
b = float(input(" nhập số b: "))
if a == 0 and b == 0:
    print(" pt có vô số nghiệm")
elif a == 0 and b != 0:
    print(" pt vô nghiệm")
else:
    print(" pt có 1 nghiệm x=", -b/a)
