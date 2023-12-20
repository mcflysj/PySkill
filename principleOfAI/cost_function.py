import dataset
import matplotlib.pyplot as plt
import numpy as np

"""
参数自适应调整方式，引入回归分析以及现代神经网络精髓之一的代价函数，
代价函数为一元二次方程e=a*w**2 + b*w + c
用初中数学知识抛物线顶点坐标公式搞定了代价函数最低点的求解,
该方法缺点为耗资源，目前主流方法为梯度下降
梯度下降：根据曲线不同处“斜率”去调整w的方式，梯度比斜率能表示的维度更高
"""

xs, ys = dataset.get_beans(100)

# 配置图像
plt.title("Size-Toxicity Function", fontsize=12)
plt.xlabel("Bean Size")  # 设置横坐标的名字
plt.ylabel("Toxicity")  # 设置纵坐标的名字

plt.scatter(xs, ys)

w = 0.1
y_pre = w * xs

plt.plot(xs, y_pre)

plt.show()

es = (ys - y_pre) ** 2
sum_e = np.sum(es)
sum_e = (1 / 100) * sum_e

ws = np.arange(0, 3, 0.1)
es = []
for w in ws:
    y_pre = w * xs
    e = (1 / 100) * np.sum((ys - y_pre) ** 2)
    es.append(e)

# 绘制w和方差e的图像，即代价函数图像
plt.title("Cost Function", fontsize=12)
plt.xlabel("w")  # 设置横坐标的名字
plt.ylabel("e")  # 设置纵坐标的名字
plt.scatter(ws, es)
plt.show()

# 用抛物线顶点坐标公式求解最低点的w
w_min = np.sum(xs * ys) / np.sum(xs * xs)
print("e最小点的w值为: ", str(w_min))

# 把最低点的值带回预测函数中
y_pre = w_min * xs

# 配置图像
plt.title("Size-Toxicity Function", fontsize=12)
plt.xlabel("Bean Size")  # 设置横坐标的名字
plt.ylabel("Toxicity")  # 设置纵坐标的名字
plt.scatter(xs, ys)
plt.plot(xs, y_pre)
plt.show()

