"""
-*- coding: utf-8 -*-
@Time : 2021/10/25 下午 12:02
@Author : sunguoqi
@Website : https://sunguoqi.com
@Github: https://github.com/sun0225SUN
"""
x = 2
num = 2
res = 0
next = 0
for i in range(num):
    next += x * 10 ** i
    res += next
print(res)
