# 线性回归梯度下降法

# 引入依赖
import numpy as np
import matplotlib.pyplot as plt


class Solution:
    # 定义模型的超参数
    alpha = 0.0001
    initial_w = 0
    initial_b = 0
    num_iter = 10

    # 定义损失函数
    def compute_cost(self, w, b, points):
        total_cost = 0  # 损失误差
        M = len(points)  # 点的个数
        # 逐点计算平方损失误差，然后求平均值
        for i in range(M):
            x = points[i, 0]  # 表示第一列第i个点，即xi
            y = points[i, 1]  # 表示第二列低i个点，即yi
            total_cost += (y - w * x - b) ** 2  # 这里y表示实际值，wx+b表示估计值，单个点误差的平方为(y-(wx+b))²，+=计算累加值

        return total_cost / M  # 函数返回误差的平方和的平均数（本例的损失函数可以理解为计算方差）

    # 定义核心拟合函数
    def grad_desc(self, points):
        w = self.initial_w
        b = self.initial_b
        cost_list = []
        for i in range(self.num_iter):
            cost_list.append(self.compute_cost(w, b, points))
            w, b = self.step_grad_desc(w, b, points)

        return [w, b, cost_list]

    # 每次迭代时算法
    def step_grad_desc(self, current_w, current_b, points):
        sum_grad_w = 0
        sum_grad_b = 0
        M = len(points)

        # 对每个点，带入公式求和
        for i in range(M):
            x = points[i, 0]
            y = points[i, 1]
            sum_grad_w += (current_w * x + current_b - y) * x
            sum_grad_b += current_w * x + current_b - y

        # 根据公式求当前梯度
        grad_w = 2 / M * sum_grad_w
        grad_b = 2 / M * sum_grad_b

        updated_w = current_w - self.alpha * grad_w
        updated_b = current_b - self.alpha * grad_b

        return updated_w, updated_b


# 测试
if __name__ == '__main__':
    # 创建一个解决方案对象
    solution = Solution()
    # 导入数据
    points = np.genfromtxt('data.csv', delimiter=',')
    # 提取两列数据
    x = points[:, 0]
    y = points[:, 1]
    # 利用plt画出散点图
    plt.scatter(x, y)
    plt.show()

    # 求得x和y所建立的线性回归方程中的参数w和b
    w, b, cost_list = solution.grad_desc(points)

    # 打印出参数的值
    print("w is:", w)
    print("b is:", b)
    print("cost is:", cost_list[-1])

    # 画出梯度变化过程
    plt.plot(cost_list)
    plt.show()

    # 画出散点图
    plt.scatter(x, y)
    # 针对每一个x,计算出预测的y值
    pred_y = w * x + b
    # 画出拟合线
    plt.plot(x, pred_y, c='r')
    # 展示
    plt.show()
