"""
-*- coding: utf-8 -*-
@Time : 2021/10/23 上午 8:27
@Author : sunguoqi
@Website : https://sunguoqi.com
@Github: https://github.com/sun0225SUN
"""


# 求所有水仙花数
class Solution:
    def judge(self, number):
        gewei = number % 10
        shiwei = number // 10 % 10
        baiwei = number // 100
        lifang = pow(gewei, 3) + pow(shiwei, 3) + pow(baiwei, 3)
        if number == lifang:
            print(number)
        else:
            pass


if __name__ == '__main__':
    solution = Solution()
    for number in range(100, 1000):
        solution.judge(number)

# for i in range(100, 1000):
#     a = i // 100
#     b = (i - a * 100) // 10
#     c = (i - a * 100 - b * 10)
#     if i == pow(a, 3) + pow(b, 3) + pow(c, 3):
#         print(i)
