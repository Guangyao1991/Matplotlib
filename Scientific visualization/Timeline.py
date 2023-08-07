# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import os

config = {"font.size": 10}
plt.rcParams.update(config)

config = {
    "text.usetex": True,
    "font.family": "serif",
}
plt.rcParams.update(config)

dir_path = os.path.dirname(__file__)


def annotate(ax, x, y, text, fc="#ff7777", y0=0):
    y = y - 0.5
    ax.annotate(
        " " + text + " ",
        xy=(x, y),
        xycoords="data",  # Use the coordinate system of the object being annotated
        xytext=(0, 12),
        textcoords="offset points",
        color="white",
        size="x-small",
        va="center",
        ha="center",
        weight="bold",
        bbox=dict(boxstyle="round", fc=fc, ec="none"),
        arrowprops=dict(
            arrowstyle="wedge,tail_width=1.", fc=fc, ec="none", patchA=None
        ),
    )
    plt.plot([x, x], [y, y0], color="black", linestyle=":", linewidth=0.75)  # 数直线


fig = plt.figure(figsize=(5, 2))
ax = fig.add_subplot(111, xlim=(2002.5, 2021.5), ylim=(0, 6.5), yticks=([]))
ax.tick_params("x", labelsize="x-small", which="major")
ax.plot([2002.5, 2021.5], [0, 0], color="black", linewidth=1.0, clip_on=False)  # 底线
X = np.arange(2003, 2022)  # 画底线上的空心点
Y = np.zeros(len(X))
plt.scatter(
    X,
    Y,
    s=50,
    linewidth=1.0,
    zorder=10,  # 避免被遮挡
    clip_on=False,  #! 绘图对象将受到剪切的影响。这意味着绘图对象将被限制在图形区域内，超出区域的部分将被裁剪掉。
    edgecolor="black",
    facecolor="white",
)

annotate(ax, 2021, 4, "3.4")
annotate(ax, 2020, 3, "3.3")
annotate(ax, 2019, 4, "3.2", y0=2.5)
annotate(ax, 2019, 2, "3.1")
annotate(ax, 2018, 3, "3.0", y0=1.5)
annotate(ax, 2018, 1, "2.2", fc="#777777")
annotate(ax, 2017, 4, "2.1", y0=2.5)
annotate(ax, 2017, 2, "2.0")
annotate(ax, 2015, 2, "1.5")
annotate(ax, 2014, 1, "1.4")
annotate(ax, 2013, 2, "1.3")
annotate(ax, 2012, 1, "1.2")
annotate(ax, 2011, 3, "1.1", y0=2.5)
annotate(ax, 2011, 2, "1.0")
annotate(ax, 2009, 1, "0.99")
annotate(ax, 2003, 1, "0.10")

for tmp in ["left", "right", "top", "bottom"]:
    ax.spines[tmp].set_visible(False)

ax.set_xticks(np.arange(2003, 2022, 2))  # 标签
ax.tick_params(axis="x", pad=7)

# h1: 上方横线
x0, x1 = 2002.5, 2011.9
ax.plot([x0, x1], [5, 5], color="black", linewidth=1, marker="|", clip_on=False)
ax.text((x0 + x1) / 2, 5.1, "J.D. Hunter", ha="center", va="bottom", size="x-small")

x0, x1 = 2012.1, 2017.9
ax.plot([x0, x1], [5, 5], color="black", linewidth=1, marker="|", clip_on=False)
ax.text(
    (x0 + x1) / 2,
    5.1,
    "M. Droettboom",
    ha="center",
    va="bottom",
    size="x-small",
)

x0, x1 = 2014.1, 2021.5
ax.plot([x0, x1 + 1], [6, 6], color="black", linewidth=1, marker="|")
ax.text((x0 + x1) / 2, 6.1, "T. Caswell", ha="center", va="bottom", size="x-small")


fig_path = os.path.join(dir_path, "matplotlib-timeline.pdf")
plt.savefig(fig_path)
