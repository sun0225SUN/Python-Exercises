# 问题描述
# 给定一个字符串（以字符数组形式）和一个偏移量，根据偏移量原地从左向右旋转字符串
# 例：str='abcdefg' offset=3 输出str='efgabcd'

# 算法思路
# 处理字符串 ‘abcdefg’ offset=3 ——> efgabcd
# 思路：用切片截取字符串然后拼接

class Solution:
    def rotateString(self, str, offset):
        str1 = str[-offset:]
        str2 = str[:-offset]
        return str1 + str2


if __name__ == '__main__':
    str = input("请输入一串字符串：")
    offset = int(input("请输入偏移量："))
    solution = Solution()
    print("旋转后的字符串为{0}".format(solution.rotateString(str, offset)))

#吐槽一下，书上的参考答案好麻烦，我不（李姐）
# 唯一的好，是当用户输入的偏移量大于字符串长度的时候，按照取余后反转，
# 可是题目，好吧，好像需要执行这个机制那我也可以改一下offset
# offset=offset%len(str)
