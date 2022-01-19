import seaborn as sns

import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates

import pandas as pd

def bar_plots(x, y, df, title, subtitle, xlabel, ylabel):
    sns.set_theme(style="whitegrid")
    f, ax = plt.subplots(figsize=(15, 6))
    ax = sns.barplot(x=x, y=y, data=df)
    ax = ax.set_xticklabels(ax.get_xticklabels(),rotation = 20, size=9)
    plt.title(title,fontsize=14, style="italic")
    plt.suptitle(subtitle, weight="bold").set_fontsize('20')
    plt.xlabel(xlabel).set_fontsize('13')
    plt.ylabel(ylabel).set_fontsize('13')