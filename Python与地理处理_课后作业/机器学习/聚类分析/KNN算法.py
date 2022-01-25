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

# 引入sklearn里的数据集，iris鸢尾花
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split  # 切分数据集为训练集和测试集
from sklearn.metrics import accuracy_score  # 计算分类预测的准确率

iris = load_iris()

df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['class'] = iris.target
df['class'] = df['class'].map(
    {0: iris.target_names[0], 1: iris.target_names[1], 2: iris.target_names[2]})
df.head(10)
df.describe()

x = iris.data
y = iris.target.reshape(-1, 1)
print(x.shape, y.shape)

# 划分训练集和数据集
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.3, random_state=35, stratify=y)

print(x_train.shape, y_train.shape)
print(x_test.shape, y_test.shape)

a = np.array([[3, 2, 4, 2],
              [2, 1, 4, 23],
              [12, 3, 2, 3],
              [2, 3, 15, 23],
              [1, 3, 2, 3],
              [13, 3, 2, 2],
              [213, 16, 3, 63],
              [23, 62, 23, 23],
              [23, 16, 23, 43]])
b = np.array([[1, 1, 1, 1]])
print(a - b)
np.sum(np.abs(a - b), axis=1)
dist = np.sqrt(np.sum((a - b) ** 2, axis=1))
print(dist)


# 核心算法实现
def l1_distance(a, b):
    return np.sum(np.abs(a - b), axis=1)


def l2_distance(a, b):
    return np.sqrt(np.sum((a - b) ** 2, axis=1))


# 分类器实现
class kNN(object):
    def __init__(self, n_neighbors=1, dist_func=l1_distance):
        self.n_neighbors = n_neighbors
        self.dist_func = dist_func

    def fit(self, x, y):
        self.x_train = x
        self.y_train = y

    # 模型预测方法

    def predict(self, x):
        y_pred = np.zeros((x.shape[0], 1), dtype=self.y_train.dtype)

        # 遍历输入x数据点
        for i, x_test in enumerate(x):
            distances = self.dist_func(self.x_train, x_test)
            nn_index = np.argsort(distances)
            nn_y = self.y_train[nn_index[:self.n_neighbors]].ravel()
            y_pred[i] = np.argmax(np.bincount(nn_y))
        return y_pred


nn_index = np.argsort(dist)
print("dist: ", dist)
print("nn_index: ", nn_index)
nn_y = y_train[nn_index[:9]].ravel()
print("nn_y: ", nn_y)
print(np.bincount(nn_y))
print(np.argmax(np.bincount(nn_y)))

# 测试

knn = kNN(n_neighbors=3)
knn.fit(x_train, y_train)
y_pred = knn.predict(x_test)

print(y_test.ravel())
print(y_pred.ravel())

accuracy = accuracy_score(y_test, y_pred)

print("预测准确率：", accuracy)

knn = kNN()
knn.fit(x_train, y_train)

result_list = []

for p in [1, 2]:
    knn.dist_func = l1_distance if p == 1 else l2_distance

    for k in range(1, 10, 2):
        knn.n_neighbors = k
        y_pred = knn.predict(x_test)
        accuracy = accuracy_score(y_test, y_pred)
        result_list.append(
            [k, 'l1_distance' if p == 1 else 'l2_distance', accuracy])
df = pd.DataFrame(result_list, columns=['k', '距离函数', '预测准确率'])
df
