# 线性回归梯度下降法
# 除了算法外，其余的地方不在分析，详解可以看最小二乘法的注释解释
# 0、引入依赖
import numpy as np
import matplotlib.pyplot as plt

# 1、导入数据
points = np.genfromtxt('data.csv', delimiter=',')

# 提取points中的两列数据，分别作为x,y
x = points[:, 0]
y = points[:, 1]

# 利用plt画出散点图
plt.scatter(x, y)
plt.show()


# 2、定义损失函数
# 损失函数是稀疏的函数，另外还要传入数据的x,y
def compute_cost(w, b, points):
    total_cost = 0
    M = len(points)
    # 逐点计算平方损失误差，然后求平均值
    for i in range(M):
        x = points[i, 0]
        y = points[i, 1]
        total_cost += (y - w * x - b) ** 2
    return total_cost / M


# 3、定义函数的超参数
alpha = 0.0001
initial_w = 0
initial_b = 0
num_iter = 10


# 4、定义核心梯度下降算法函数
def grad_desc(points, initial_w, initial_b, alpha, num_iter):
    # 根据公式，w:=w+ɑ∇，需要给w参数一个初始值为0
    w = initial_w
    b = initial_b

    # 定义一个list保存所有的损失值，用来显示下降的过程
    cost_list = []

    # 迭代10次，更新,w和b
    for i in range(num_iter):
        cost_list.append(compute_cost(w, b, points))  # 将每次的损失值存入的cost_list中，后面画图展示损失值不断先将的曲线。
        w, b = step_grad_desc(w, b, alpha, points)  # 每一步w和b具体的计算算法

    return [w, b, cost_list]  # 程序范围我们需要求解的w,b和损失值列表


# 每一步的w,b的求解算法
def step_grad_desc(current_w, current_b, alpha, points):
    # 根据公式，损失函数哦关于w的梯度为（2/M）*∑(wx+b-y)*x，我们需要计算累加和，sum_grad_w意思是公式中的那部分累加和初始值为零，同理知道sum_grad_b的意思！
    sum_grad_w = 0
    sum_grad_b = 0

    M = len(points)  # 点的个数

    # 对每个点，带入公式求和
    for i in range(M):
        x = points[i, 0]  # 取第一列第一个点，即x1
        y = points[i, 1]  # 取第二列第一个点，即x2
        sum_grad_w += (current_w * x + current_b - y) * x  # 求解损失函数关于w的梯度的公式中的累加和部分
        sum_grad_b += current_w * x + current_b - y

    # 根据公式求当前梯度
    grad_w = 2 / M * sum_grad_w  # 损失函数关于参数w的梯度
    grad_b = 2 / M * sum_grad_b  # 损失函数关于参数b的梯度

    # 梯度下降，更新当前的w和b
    updated_w = current_w - alpha * grad_w  # 梯度已下降，已从山上走下来了一部分，更新现在的点的位置，即更新参数w和c参数b
    updated_b = current_b - alpha * grad_b

    return updated_w, updated_b  # 程序返回更新后的w,b


# 5、测试：运行梯度下降算法计算最优的w和b
w, b, cost_list = grad_desc(points, initial_w, initial_b, alpha, num_iter)

print("w is:", w)
print("b is:", b)

cost = compute_cost(w, b, points)
print("cost is:", cost)

# 画出变化过程
plt.plot(cost_list)
plt.show()

# 6、画出拟合曲线
plt.scatter(x, y)
# 针对每一个x,计算出预测的y值
pred_y = w * x + b

plt.plot(x, pred_y, c='r')
plt.show()
