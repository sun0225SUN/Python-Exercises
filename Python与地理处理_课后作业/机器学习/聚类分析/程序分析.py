"""
-*- coding: utf-8 -*-
@Time : 2021/10/13 下午 5:36
@Author : sunguoqi
@Website : https://sunguoqi.com
@Github: https://github.com/sun0225SUN
"""

# 引入依赖
import numpy as np
import pandas as pd

from sklearn.datasets import load_iris # 引入sklearn里的数据集，iris鸢尾花
from sklearn.model_selection import train_test_split  # 引入此模块，用来切分训练集与测试集
from sklearn.metrics import accuracy_score  # 引入此模块，用来计算分类模型预测的准确率

# 加载鸢尾花数据
iris = load_iris()

df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

# 构造DataFrame数据
# 开始构造一个DataFrame数据表，用iris.data作为每类数据，用iris.feature_names作为每列数据的表头
# 查看iris数据，查看df数据，我们就知道我们现在已经构造了一张数据表。
#
# df['class'] = iris.target
# #定义class索引，值为iris.target，iris的值有1，2，3三种类别
# df['class'] = df['class'].map({0: iris.target_names[0], 1: iris.target_names[1], 2: iris.target_names[2]})
# 映射0表示se花，1表示ve花，2表示vi花

# 上面两句话的操作就是，让原始数据中的012用target_names里的花名表示。

# df.head(10)
# 读取前10行数据
# df.describe()
# 用于生成描述性统计数据，统计数据集的集中趋势，分散和行列的分布情况，不包括 NaN值。

x = iris.data
# 令x等于鸢尾花的那个数组
y = iris.target.reshape(-1, 1)
# y是分类目标，.reshape(-1,1)让数据转换成一列，就是一维转换成二维，列数为一列

# print(x.shape, y.shape)
# 打印数据维度，正常应该x(150,4)，y(150,1)

# 划分训练集和数据集
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=35, stratify=y)

# stratify的意思是按照y里的数据进行分类，random是随机种子，生成35随机数，意思就是打乱测试集和训练集的数据，因为原先的是按照一定顺序排列的，我们训练或者预测肯定是无序的。
# 150*0.7=105   150*0.3
# print(x_train.shape, y_train.shape)
# print(x_test.shape, y_test.shape)

# # # 测试计算距离算法？？？这段代码？？？
# # 训练数据
# a = np.array([[3, 2, 4, 2],
#               [2, 1, 4, 23],
#               [12, 3, 2, 3],
#               [2, 3, 15, 23],
#               [1, 3, 2, 3],
#               [13, 3, 2, 2],
#               [213, 16, 3, 63],
#               [23, 62, 23, 23],
#               [23, 16, 23, 43]])
# # 预测数据
# b = np.array([[1, 1, 1, 1]])
#
# # print(a - b)
# # np.sum(np.abs(a - b), axis=1)
# dist = np.sqrt(np.sum((a - b) ** 2, axis=1))
# # axis为1是压缩列,即将每一行的元素相加,将矩阵压缩为一列，输出：array([15., 40., 65., 90.])
# # print(dist)

# 核心算法实现
# 欧几里得距离
def l1_distance(a, b):
    return np.sum(np.abs(a - b), axis=1)

# 曼哈顿距离
def l2_distance(a, b):
    return np.sqrt(np.sum((a - b) ** 2, axis=1))

# 分类器实现
class kNN(object):
    # 初始化属性值
    def __init__(self, n_neighbors=1, dist_func=l1_distance):
        self.n_neighbors = n_neighbors
        self.dist_func = dist_func

    # 还是定义俩属性？？？，为啥不初始化的时候一起定义呢？？？,
    def fit(self, x, y):
        self.x_train = x
        self.y_train = y

    # 模型预测方法
    def predict(self, x):
        # 初始化预测分类目标数组，都是0一列数
        y_pred = np.zeros((x.shape[0], 1), dtype=self.y_train.dtype)

        # 遍历输入x数据点
        for i, x_test in enumerate(x):
            # enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列
            # 计算所有训练数据距离
            distances = self.dist_func(self.x_train, x_test)
            # 得到的距离按照由近到远的距离进行排序，排列的是索引值
            nn_index = np.argsort(distances)
            # 选取最近的k个点，保存他们对应的分类类别
            nn_y = self.y_train[nn_index[:self.n_neighbors]].ravel()
            # 统计类别中出现频率最高的那个并赋值给y_pred
            y_pred[i] = np.argmax(np.bincount(nn_y))
        return y_pred


# nn_index = np.argsort(dist)
# # print("dist: ", dist)
# # print("nn_index: ", nn_index)
#
# nn_y = y_train[nn_index[:9]].ravel()
# print("nn_y: ", nn_y)
# print(np.bincount(nn_y))
# print(np.argmax(np.bincount(nn_y)))


# 测试

# knn = kNN(n_neighbors=3)
# knn.fit(x_train, y_train)
# y_pred = knn.predict(x_test)
#
# print(y_test.ravel())
# print(y_pred.ravel())
#
# accuracy = accuracy_score(y_test, y_pred)
#
# print("预测准确率：", accuracy)



knn = kNN()
knn.fit(x_train, y_train)

result_list = []

for p in [1, 2]:
    knn.dist_func = l1_distance if p == 1 else l2_distance

    for k in range(1, 10, 2):
        knn.n_neighbors = k
        y_pred = knn.predict(x_test)
        accuracy = accuracy_score(y_test, y_pred)
        result_list.append([k, 'l1_distance' if p == 1 else 'l2_distance', accuracy])
df = pd.DataFrame(result_list, columns=['k', '距离函数', '预测准确率'])