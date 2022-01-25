"""
-*- coding: utf-8 -*-
@Time : 2021/10/23 上午 8:27
@Author : sunguoqi
@Website : https://sunguoqi.com
@Github: https://github.com/sun0225SUN
"""


class Solution:
    def compute(self, x, num):
        next = 0
        res = 0
        for i in range(num):
            next += x * 10 ** i
            res += next
        return res

        # 这里有个小tip，就是range后面的参数个算法的问题
        # 也可以这样写

        # next = 0
        # res = 0
        # for i in range(1, num + 1):
        #     next += x * 10 ** (i - 1)
        #     res += next
        # return res


if __name__ == '__main__':
    solution = Solution()
    x = int(input("请输入数字："))
    num = int(input("请输入相加个数："))
    print(solution.compute(x, num))

# 简单写法，直接写！
# a = int(input("请输入数字："))
# b = int(input("请输入相加个数："))
# next, res = 0, 0
# for i in range(1, b + 1):
#     next += a * 10 ** (i - 1)
#     res += next
# print(res)
