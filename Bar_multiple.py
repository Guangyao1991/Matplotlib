# -*- encoding: utf-8 -*-
"""
@File    :   Bar.py
@Time    :   2023/06/03 19:22:26
@Author  :   Guangyao Zhao
@Contact :   zhaoguangyao1991@163.com
@Desc    :   Multicolumn of Bar plot
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


dir_path = os.path.dirname(__file__)
# file_path = os.path.join(dir_path,"") #TODO: input your file path
# dataset = pd.read_csv(file_path, index_col=[0], header=[0])

# h1: dummy dataset
np.random.seed(1)
dataset = np.random.normal(loc=0.5, scale=0.1, size=(6, 2))
dataset = pd.DataFrame(
    dataset, columns=["SHAP", "F score"], index=list("abcdef")
).sort_values(by=["SHAP"], ascending=False)

# h1: figure
fig = plt.figure(figsize=(8, 6))
ax1 = fig.add_subplot(111)
color_li = ["#E71D36", "#FFBC42", "#2EC4B6", "#56a0d3", "#92C5DE", "#b4a996"]
width = 1 / (dataset.shape[0] + 1.5)  # bar width
x = np.arange(dataset.shape[1])  # position
for i in range(dataset.shape[0]):
    tmp = ax1.bar(
        x + i * width,
        dataset.iloc[i, :],
        width=width,
        align="edge",  # center, edge
        color=color_li[i],
        edgecolor="k",
        label=dataset.index[i],
    )
    ax1.bar_label(tmp, fmt="%.2f", padding=3)  # label

# settings
ax1.set_ylim(0, 1.2)  # ax1.set_ylim(0, 1.0)
ax1.set_ylabel(
    ylabel="Feature importance", position=(0, 0.5 / 1.2), ha="center"
)  # ax1.set_ylabel("Feature importance")
ax1.tick_params(axis="both", which="major", direction="inout")
ax1.tick_params(axis="x", which="both", bottom=False)  # remove original x label
ax1.set_xticks(
    x + width / 2 * dataset.shape[0],  # position
    dataset.columns,  # label
)
ax1.margins(x=0.05)  # margin between spine and bar
ax1.legend(ncol=2)

# customize y ticks
locator_major = plt.FixedLocator(locs=np.arange(0, 11, 2) / 10)  # major ticks
ax1.yaxis.set_major_locator(locator=locator_major)
locator_minor = plt.FixedLocator(locs=np.arange(1, 10, 2) / 10)  # minor ticks
ax1.yaxis.set_minor_locator(locator=locator_minor)

# h2: savefig
fig_path = os.path.join(dir_path, "Results", "Bar_multiple.pdf")
fig.savefig(fig_path)
