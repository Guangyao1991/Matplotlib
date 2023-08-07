# -*- encoding: utf-8 -*-
"""
@File    :   Scatter.py
@Time    :   2023/07/20 00:00:50
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
dataset = np.random.normal(loc=0.5, scale=0.2, size=(10, 2))


# h1: figure
fig = plt.figure(figsize=(8, 6))
ax1 = fig.add_subplot(111)

ax1.scatter(
    x=dataset[:, 0],
    y=dataset[:, 1],
    color="#DA8277",
    marker="o",
    s=100,
    alpha=0.7,
    edgecolors="black",
    linewidths=0.5,
)

# settings
ax1.set_xlabel("x label")
ax1.set_ylabel("y label")
ax1.set_xlim(0, 1)
ax1.set_ylim(0, 1)
ax1.tick_params(axis="both", which="major", direction="inout")

fig_path = os.path.join(dir_path, "Results", "Scatter.pdf")
fig.savefig(fig_path)
