"""
-*- coding: utf-8 -*-
@Time : 2021/10/23 上午 8:27
@Author : sunguoqi
@Website : https://sunguoqi.com
@Github: https://github.com/sun0225SUN
"""


# 求所有水仙花数
class Solution:
    def judge_3(self, number):
        gewei = number % 10
        shiwei = number // 10 % 10
        baiwei = number // 100 % 10
        lifang = pow(gewei, 3) + pow(shiwei, 3) + pow(baiwei, 3)
        if number == lifang:
            print(number)
        else:
            pass

    def judge_4(self, number):
        gewei = number % 10
        shiwei = number // 10 % 10
        baiwei = number // 100 % 10
        qianwei = number // 1000
        lifang = pow(gewei, 4) + pow(shiwei, 4) + \
            pow(baiwei, 4) + pow(qianwei, 4)
        if number == lifang:
            print(number)
        else:
            pass


if __name__ == '__main__':
    solution = Solution()
    for number in range(100, 10000):
        solution.judge_3(number)
        if number >= 1000:
            solution.judge_4(number)
