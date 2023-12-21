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

#y = 0.5*x
w = 0.5
y_pre = w * xs

plt.plot(xs, y_pre)

plt.show()
