# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: Creative Commons BY-NC-SA International 4.0
# ----------------------------------------------------------------------------
import os

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.transforms import ScaledTranslation, blended_transform_factory

config = {"font.size": 12}
plt.rcParams.update(config)
dir_path = os.path.dirname(__file__)

fig = plt.figure()

ax = fig.add_subplot(1, 1, 1, aspect=1)
ax.set_xlim(0, 10)
ax.set_xticks(range(11))
ax.set_ylim(0, 5)
ax.set_xticks(range(11))


# h1: 混合坐标系
point = 1 / 72
fontsize = 12
dx, dy = 0, -1.5 * fontsize * point
offset = ScaledTranslation(dx, dy, fig.dpi_scale_trans)
transform = blended_transform_factory(ax.transData, ax.transAxes + offset)

for x in range(11):
    plt.text(x, 0, "↑", transform=transform, ha="center", va="top", fontsize=fontsize)


fig_path = os.path.join(dir_path, "Transforms blend.pdf")
plt.savefig(fig_path)
