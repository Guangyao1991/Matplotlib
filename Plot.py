# -*- encoding: utf-8 -*-
"""
@File    :   plot.py
@Time    :   2023/07/20 00:07:28
@Author  :   Guangyao Zhao 
@Contact :   zhaoguangyao1991@163.com
@Desc    :   
"""


import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


config = {
    "font.size": 20,
}
plt.rcParams.update(config)


# h1: dataset
dir_path = os.path.dirname(__file__)
# file_path = os.path.join(dir_path,"") #TODO: input your file path
# dataset = pd.read_csv(file_path, index_col=[0], header=[0])

# h1: dummy dataset
np.random.seed(1)
x = np.linspace(0, 10, 100) - np.random.rand(100) / 10
y = np.sin(x)

# h1: figure
fig = plt.figure(figsize=(8, 6))
ax1 = fig.add_subplot(111)

ax1.plot(
    x,
    y,
    color="#DA8277",
)

# settings
ax1.set_xlabel("x")
ax1.set_ylabel("sin(x)")
ax1.set_xlim(0, 10)
ax1.set_ylim(-1.02, 1.02)
ax1.tick_params(axis="both", which="major", direction="inout")

fig_path = os.path.join(dir_path, "Results", "Plot.pdf")
fig.savefig(fig_path)
