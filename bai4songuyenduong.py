# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:41:05 2024

@author: Nguyễn Phú Quỳnh Như
"""

n=int(input(" nhập số nguyên dương n có 2 chữ số: "))
chu_so_hang_chuc= n // 10
chu_so_hang_don_vi= n % 10
tong_cac_chu_so_cua_n= chu_so_hang_chuc + chu_so_hang_don_vi
if 10 <= n <= 99:
    print("tổng các chữ số của n là: ", tong_cac_chu_so_cua_n)
else:
    print(" nhập lại số nguyên có hai chữ số!")
    


