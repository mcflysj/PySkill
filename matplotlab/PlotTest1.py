import matplotlib.pyplot as plt
import random

from pylab import mpl
# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
# 设置正常显示符号
mpl.rcParams["axes.unicode_minus"] = False

# 0.准备数据
x = range(60)
y_haikou = [random.uniform(25,30) for i in x]

# 1.创建画布
plt.figure(figsize=(20, 8), dpi=100)

# 2.绘制图像
plt.plot(x, y_haikou)

# 2.1 添加x，y轴刻度
# 设置x，y轴刻度
x_ticks_lable = ["11点{}分".format(i) for i in x]
y_ticks = range(40)

# 修改x，y轴坐标刻度显示
plt.xticks(x[::5], x_ticks_lable[::5])
plt.yticks(y_ticks[::5])

# 2.2 添加网格显示
plt.grid(True, linestyle="--", alpha=1)

# 2.3 添加描述信息
plt.xlabel("时间")
plt.ylabel("温度")
plt.title("中午11点-12点海口温度变化图", fontsize=20)

# 2.4 图像保存
plt.savefig("./out/PlotTest1.png")

# 3.图像显示
plt.show()