# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 19:08:41 2024

@author: Nguyễn Phú Quỳnh Như

"""
can_nang= float(input(" nhập số cân nặng: "))
chieu_cao= float(input(" nhập số chiều cao: "))
cong_thuc_bmi=round( can_nang / chieu_cao ** 2, 2)
print(" vậy số đo sức khỏe bmi của bạn là: ", cong_thuc_bmi)

