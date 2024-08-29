# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 12:11:21 2024

@author: Nguyễn Phú Quỳnh Như
"""

import math
nhap = input("Nhập hình: ")
"n" == "Hình chữ nhật"
"v" == "Hình vuông"
"t" == "Hình tròn"
if nhap == "n":
    print("Tính P và S của hình chữ nhật")
    a = int(input("Nhập chiểu rộng = "))
    b = int(input("Nhập chiểu dài = "))
    P = (a + b) * 2
    S = a * b
    print(f"Kết quả {P}  {S} ")
elif nhap == "v":
    print("Tính P và S của hình vuông")
    a = int(input("Nhập độ dài của cạnh = "))
    P = a * 4
    S = pow(a, 2)
    print(f"Kết quả {P}  {S} ")
else:
    print("Tính P và S của hình tròn")
    r = int(input("Nhập bán kính của đường tròn = "))
    P = round(2 * math.pi * r, 2)
    S = round(pow(r, 2) * math.pi, 2)
    print(f"Kết quả {P}  {S} ")