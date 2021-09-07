# 问题描述
# 合并两个升序的数组A和B，形成一个数组，新数组也要排序
# 示例A=[1,2,3,4],B=[2,4,5,6],输出[1,2,2,3,4,4,5,6]

class Solution:
    def mergeSortedArray(self, A, B):
        i, j = 0, 0
        C=[]
        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                C.append(A[i])
                i += 1
            else:
                C.append(B[j])
                j += 1
        while i < len(A):
            C.append(A[i])
            i += 1
        while j < len(B):
            C.append(B[j])
            j += 1
        return C


if __name__ == '__main__':
    str1 = input("请输入一串数字，中间用逗号隔开\n请输入：")
    str2 = input("请输入第第二串数字\n请输入：")
    A = str1.split(',')
    B = str2.split(',')
    new_A = []
    new_B = []
    for n in A:
        new_A.append(int(n))
    A = new_A
    for n in B:
        new_B.append(int(n))
    B = new_B
    A.sort()
    B.sort()
    solution = Solution()
    print("第一组数据升序排列为{0}\n第二组数据升序排列后为{1}\n合并排序后为{2}".format(A, B, solution.mergeSortedArray(A, B)))
