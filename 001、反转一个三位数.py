# 反转一个三位数
# 问题描述：输入number=123；输出321

class Solution:
    # 参数为number,例:123
    # 返回结果
    def reverseInteger(self, number):
        g = number % 10
        s = number // 10 % 10
        b = number // 100

        return g * 100 + s * 10 + b * 1


if __name__ == '__main__':
    solution = Solution()
    num = int(input("请输入一个三位数："))
    print("您输入的三位数反转后为：{0}".format(solution.reverseInteger(num)))
