import dataset
import matplotlib.pyplot as plt
import numpy as np

"""
随机梯度下降
# 1、导入库
# 2、生成数据
# 3、配置绘图
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

for _ in range(100):
    for i in range(100):
        x = xs[i]
        y = ys[i]
        # a=x^2
        # b=-2*x*y
        # c=y^2
        # 斜率k=2aw+b
        k = 2 * (x ** 2) * w + (-2 * x * y)
        alpha = 0.1
        w = w - alpha * k
        plt.clf()  # 清空窗口
        plt.scatter(xs, ys)
        y_pre = w * xs  # 重新计算预测值
        plt.xlim(0, 1)  # 限制x坐标范围
        plt.ylim(0, 1.2)  # 限制y坐标范围
        plt.plot(xs, y_pre)
        plt.pause(0.01)  # 暂停时间


# 此外还有固定步长下降，批量固定下降