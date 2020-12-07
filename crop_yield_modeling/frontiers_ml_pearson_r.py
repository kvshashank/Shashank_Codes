# -*- coding: utf-8 -*-
"""Frontiers_ML_pearson_r.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XZ41eTuAi7nzwr7LZZnpRqMYh7oVvulc
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

sns.set(font_scale=1.5)
data = pd.read_csv("combined_indices.csv", header=0)
data = data.drop("Year", axis=1)
labels=["GSP (mm)","GDD ($^O$C)","GST$_{max}$ ($^O$C)", "GST$_{min}$ ($^O$C)", "Frost days",
        "Summer Days","Heat Wave index", "Cold Wave index", "Longest Dry Spell", "Longest Wet Spell", "prcp95p"]
corr = data.corr()

mask = np.zeros_like(corr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True

f, ax = plt.subplots(figsize=(10,8))

cmap = sns.diverging_palette(220, 10, as_cmap=True)
ax = sns.heatmap(corr, mask=mask, cmap=cmap, center=0, square=True, 
            linewidths=0.5, cbar_kws={"shrink": 0.7}, yticklabels=labels, xticklabels=labels)
symbol = r'$\rho$'
title = "Pearson Correlation Coefficient (" + symbol + ")"
plt.title(title)
plt.subplots_adjust(left=0.3, bottom=0.3)
plt.savefig("pearson_r.png")

print r'$\alpha > \beta$'
