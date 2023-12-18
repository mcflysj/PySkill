import dataset
from matplotlib import pyplot as plt

xs, ys = dataset.get_beans(100)
print(xs)
print(ys)

# 配置图像
plt.title("Size-Toxicity Function", fontsize=12)
plt.xlabel("Bean Size")  # 设置横坐标的名字
plt.ylabel("Toxicity")  # 设置纵坐标的名字

plt.scatter(xs, ys)

# Rosenblatt感知器流程
# 1、输入自变量x
# 2、因变量y = w * x
# 3、标准答案 - y = 误差e
# 4、w + alpha * 误差e * x = 新w (注：alpha为学习率，乘以x是处理y为负值时的情况)
# 5、w = 新w
# 6、循环至第1步

w = 0.5  # 初始设置

for i in range(100):
    for i in range(100):
        x = xs[i]
        y = ys[i]
        y_pre = w * x
        e = y - y_pre
        alpha = 0.05
        w = w + alpha * e * x

y_pre = w * xs

plt.plot(xs, y_pre)

plt.show()
