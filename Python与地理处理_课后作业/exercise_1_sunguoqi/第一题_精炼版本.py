"""
-*- coding: utf-8 -*-
@Time : 2021/10/25 上午 11:07
@Author : sunguoqi
@Website : https://sunguoqi.com
@Github: https://github.com/sun0225SUN
"""

for num in range(100, 100000):
    str_num = str(num)
    sum = 0
    n = len(str_num)
    for i in str_num:
        sum += int(i) ** n
    if num == sum:
        print(sum, end='、')
