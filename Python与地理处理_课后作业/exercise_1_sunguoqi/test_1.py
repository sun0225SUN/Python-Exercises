"""
-*- coding: utf-8 -*-
@Time : 2021/10/23 上午 8:27
@Author : sunguoqi
@Website : https://sunguoqi.com
@Github: https://github.com/sun0225SUN
"""


class Solution:
    def judge(self, n):
        # 创建一个空列表，存储符合条件的结果
        list_res = []
        # 循环遍历整个区间
        for i in range(10 ** (n - 1), 10 ** n):
            # 为了获取每一位上的值，这里将i转换成字符串，用字符串索引获得各各位数上的值
            str1 = str(i)
            sum1 = 0
            # 遍历字符串
            for j in str1:
                num = int(j)
                sum1 += num ** n
            # 判断
            if i == sum1:
                list_res.append(i)
        return list_res


if __name__ == '__main__':
    solution = Solution()
    res = []
    n = len(input("请输入区间最大值："))
    for i in range(3, n):
        res.extend(solution.judge(i))
    print(res)

# 直接写
# list2 = []
# for i in range(10 ** (n - 1), 10 ** n):
#     str1 = str(i)
#     sum1 = 0
#     for j in str1:
#         num = int(j)
#         sum1 += num ** n
#     if i == sum1:
#         list2.append(i)
# print(list2)
