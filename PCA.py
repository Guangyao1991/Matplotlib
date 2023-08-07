import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# h1: dataset
dir_path = os.path.dirname(__file__)
# file_path = os.path.join(dir_path, "Dataset.csv") #TODO: input your file path
# dataset = pd.read_csv(file_path, header=[0], index_col=[0])

# h1: dummy dataset
np.random.seed(1)
dataset = np.random.normal(loc=0.5, scale=0.1, size=(3, 4))
dataset = pd.DataFrame(StandardScaler().fit_transform(dataset))  # standardization


# h1: PCA
pca = PCA(n_components=2)
PCA_data = pd.DataFrame(pca.fit_transform(dataset))  # PCA
components = pd.DataFrame(pca.components_)  # matrix: (2,samples)
explained_variance_ratio = pd.Series(
    pca.explained_variance_ratio_, index=["PCA_1", "PCA_2"]
)  # explained variance ratio


# h1: figure
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111)

color_li = [
    "#FF0000",
    "#00FF00",
    "#0000FF",
]
for i1 in range(PCA_data.shape[0]):
    ax.scatter(
        x=PCA_data.iloc[i1, 0],
        y=PCA_data.iloc[i1, 1],
        marker="o",
        s=100,
        alpha=0.6,
        edgecolors="black",
        linewidths=0.5,
        c=color_li[i1],
        label=PCA_data.index.to_list()[i1],
    )
ax.legend(loc="upper right", ncol=1)

# h2: plot vector
for component in components.columns:
    tmp = components[component]
    ax.annotate(
        xy=(0, 0),
        xytext=(tmp.values[0], tmp.values[1]),
        text=component,
        fontsize=8,
        # bbox=dict(boxstyle="round", fc="w", alpha=0.8),
        arrowprops=dict(arrowstyle="<|-", linewidth=1, color="r"),
    )
# settings
ax.set_xlabel(f"PCA 1 ({round(explained_variance_ratio['PCA_1'],2)})")
ax.set_ylabel(f"PCA 2 ({round(explained_variance_ratio['PCA_2'],2)})")
ax.tick_params(axis="both", which="major", direction="inout")

fig_path = os.path.join(dir_path, "Results", "PCA.pdf")
fig.savefig(fig_path)
