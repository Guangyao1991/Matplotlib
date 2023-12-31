# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator, MultipleLocator, FuncFormatter
import os

config = {"font.size": 10, "font.family": "Georgia"}
plt.rcParams.update(config)

config = {
    "text.usetex": True,
    "font.family": "serif",
}
plt.rcParams.update(config)

dir_path = os.path.dirname(__file__)

# h1: 数据点
np.random.seed(123)
X = np.linspace(0.5, 3.5, 100)
Y1 = 3 + np.cos(X)
Y2 = 1 + np.cos(1 + X / 0.75) / 2
Y3 = np.random.uniform(Y1, Y2, len(X))


# h1: figure
fig = plt.figure(figsize=(8, 8), facecolor='#e9e7ef')
ax = fig.add_subplot(1, 1, 1, aspect=1)

# h2: general settings
ax.set_xlim(0, 4)
ax.set_ylim(0, 4)
ax.tick_params(which="major", width=1.0, length=10)
ax.tick_params(which="minor", width=1.0, labelsize=10, length=5)
ax.grid(linestyle="--", linewidth=0.5, color=".25", zorder=-10)
ax.plot(X, Y1, c=(0.25, 0.25, 1.00), lw=2, label="Blue signal", zorder=10)
ax.plot(X, Y2, c=(1.00, 0.25, 0.25), lw=2, label="Red signal")
ax.plot(X, Y3, linewidth=0, marker="o", markerfacecolor="w", markeredgecolor="k")
ax.set_title("Anatomy of a figure", fontsize=20, verticalalignment="bottom")
ax.set_xlabel("X axis label")
ax.set_ylabel("Y axis label")
ax.legend(loc='upper right')


# h2: tricky settings
def minor_tick(x, pos):
    return "%.2f" % x  #! 注意这种并不是取余。"%.2f"表示格式，% 表示要格式化的意思，x 表示格式化的对象


ax.xaxis.set_major_locator(MultipleLocator(1))  # 单位长度的大小
ax.xaxis.set_minor_locator(AutoMinorLocator(4)) #! 副刻度的个数
ax.xaxis.set_minor_formatter(FuncFormatter(minor_tick))  #! 可以使用方程格式化
ax.yaxis.set_major_locator(MultipleLocator(1))
ax.yaxis.set_minor_locator(AutoMinorLocator(4))
ax.tick_params(axis='both', which='major', direction='inout')

# h2: tricky settings
def circle(x, y, radius=0.15):
    from matplotlib.patches import Circle
    from matplotlib.patheffects import withStroke  #! 击断效果

    circle = Circle(
        (x, y),
        radius,
        clip_on=False,
        zorder=10,  #! 层级高一点
        linewidth=1,
        edgecolor="black",
        facecolor=(0, 0, 0, 0.0125),
        path_effects=[
            withStroke(linewidth=3, foreground="w")
        ],  #! linewidth表示的是截断的线宽是多少; foreground 是颜色
    )
    ax.add_artist(circle)  # 添加圆


def text(x, y, text):
    ax.text(
        x,
        y,
        text,
        backgroundcolor="white",
        # fontname="Yanone Kaffeesatz", fontsize="large",
        ha="center",
        va="top",
        weight="regular",
        color="#000099",
    )


# Minor tick
circle(0.50, -0.10)
text(0.50, -0.32, "Minor tick label")

# Major tick
circle(-0.03, 4.00)
text(0.03, 3.80, "Major tick")

# Minor tick
circle(0.00, 3.50)
text(0.00, 3.30, "Minor tick")

# Major tick label
circle(-0.15, 3.00)
text(-0.15, 2.80, "Major tick label")

# X Label
circle(1.80, -0.27)
text(1.80, -0.45, "X axis label")

# Y Label
circle(-0.27, 1.80)
text(-0.27, 1.6, "Y axis label")

# Title
circle(1.60, 4.13)
text(1.60, 3.93, "Title")

# Blue plot
circle(1.75, 2.80)
text(1.75, 2.60, "Line\n(line plot)")

# Red plot
circle(1.20, 0.60)
text(1.20, 0.40, "Line\n(line plot)")

# Scatter plot
circle(3.20, 1.75)
text(3.20, 1.55, "Markers\n(scatter plot)")

# Grid
circle(3.00, 3.00)
text(3.00, 2.80, "Grid")

# Legend
circle(3.70, 3.80)
text(3.70, 3.60, "Legend")

# Axes
circle(0.5, 0.5)
text(0.5, 0.3, "Axes")

# Figure
circle(-0.3, 0.65)
text(-0.3, 0.45, "Figure")

# h2: Spines annotation
color = "#000099"
ax.annotate(
    "Spines",
    xy=(4.0, 0.35),
    xytext=(3.3, 0.5),
    color=color,
    weight="regular",  # fontsize="large", fontname="Yanone Kaffeesatz",
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color=color),
)

ax.annotate(
    "",
    xy=(3.15, 0.0),
    xytext=(3.45, 0.45),
    color=color,
    weight="regular",  # fontsize="large", fontname="Yanone Kaffeesatz",
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color=color),
)

fig_path = os.path.join(dir_path, "Anatomy.pdf")
fig.savefig(fig_path)
