# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: Creative Commons BY-NC-SA International 4.0
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.transforms import ScaledTranslation
import os

config = {"font.size": 14, "font.family": "Georgia"}
plt.rcParams.update(config)
dir_path = os.path.dirname(__file__)

# h1: figure
fig = plt.figure(figsize=(8, 6 * 2))
ax = fig.add_subplot(2, 1, 1)
plt.text(
    0.1,
    0.1,
    "A",
    fontsize="x-large",
    weight="bold",
    ha="left",
    va="baseline",
    transform=ax.transAxes, #! 以子图为单位
)

ax = fig.add_subplot(2, 1, 2)
dx, dy = 10 / 72, 10 / 72
offset = ScaledTranslation(dx, dy, fig.dpi_scale_trans) # 添加 offset，以 pixel 为单位

plt.text(
    0,
    0,
    "B",
    fontsize="x-large",
    weight="bold",
    ha="left",
    va="baseline",
    transform=ax.transAxes + offset,
)

fig_path = os.path.join(dir_path, "Transformed letter.pdf")
plt.savefig(fig_path)
