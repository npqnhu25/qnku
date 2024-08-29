# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 12:07:41 2024

@author: Nguyễn Phú Quỳnh Như
"""
chucai = input("nhập chữ cái bất kì")
if chucai.islower():
    chucai = chucai.upper()
elif chucai.isupper():
    chucai = chucai.lower()
else:
    print("đây không phải là chữ cái hợp lệ")
print(" hợp lệ ",chucai)
