# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import os

config = {"font.family": "Georgia"}
plt.rcParams.update(config)
dir_path = os.path.dirname(__file__)

fig, ax = plt.subplots()
for label in ax.get_xaxis().get_ticklabels():  #! 得到刻度标签对象
    label.set_fontweight("bold")
    label.set_fontfamily("Arial")


fig_path = os.path.join(dir_path, "Bold ticklabel.pdf")
plt.savefig(fig_path)
