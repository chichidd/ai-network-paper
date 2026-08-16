#!/usr/bin/env python3
import csv
from pathlib import Path

import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


HERE = Path(__file__).resolve().parent
DATA = HERE / 'data' / 'heterogeneity.csv'
OUTPUT = HERE.parent / 'figures' / 'eval_heterogeneity.pdf'

with DATA.open(encoding='utf-8', newline='') as handle:
    rows = list(csv.DictReader(handle))

plt.rcParams.update(
    {
        'font.family': 'DejaVu Sans',
        'font.size': 7.2,
        'axes.spines.top': False,
        'axes.spines.right': False,
        'pdf.fonttype': 42,
        'ps.fonttype': 42,
    }
)

partitions = ['IID', 'alpha=10', 'alpha=1', 'alpha=0.5', 'alpha=0.1']
tick_labels = ['IID', 'α=10', 'α=1', 'α=.5', 'α=.1']
datasets = [('darknet', 'Darknet', '#3B6FB6'), ('maldroid', 'MalDroid', '#DD8452')]
x = np.arange(len(partitions))

fig, axes = plt.subplots(1, 4, figsize=(7.03, 2.18))

width = 0.34
for index, (dataset, label, color) in enumerate(datasets):
    values = [
        int(next(row for row in rows if row['dataset'] == dataset and row['partition'] == partition)['usable'])
        for partition in partitions
    ]
    axes[0].bar(x + (index - 0.5) * width, values, width=width, color=color, label=label)
axes[0].set_title('(a) Accepted partitions', fontsize=8)
axes[0].set_ylabel('Accepted seeds (of 10)')
axes[0].set_ylim(0, 11.2)

for dataset, label, color in datasets:
    points = [next(row for row in rows if row['dataset'] == dataset and row['partition'] == partition) for partition in partitions]
    valid = [(position, row) for position, row in enumerate(points) if row['jsd']]
    axes[1].errorbar(
        [position for position, _ in valid],
        [float(row['jsd']) for _, row in valid],
        yerr=[float(row['jsd_ci95']) for _, row in valid],
        color=color,
        marker='o',
        markersize=3.5,
        linewidth=1.2,
        capsize=2,
        label=label,
    )
axes[1].set_title('(b) Label imbalance', fontsize=8)
axes[1].set_ylabel('Client label JSD')

darknet = [next(row for row in rows if row['dataset'] == 'darknet' and row['partition'] == partition) for partition in partitions]
axes[2].errorbar(
    x,
    [float(row['macro_f1']) for row in darknet],
    yerr=[float(row['macro_f1_ci95']) for row in darknet],
    color='#3B6FB6',
    marker='o',
    markersize=3.5,
    linewidth=1.2,
    capsize=2,
)
axes[2].set_title('(c) Darknet at 50%', fontsize=8)
axes[2].set_ylabel('Macro F1')

maldroid = [next(row for row in rows if row['dataset'] == 'maldroid' and row['partition'] == partition) for partition in partitions]
maldroid_valid = [(position, row) for position, row in enumerate(maldroid) if row['macro_f1']]
axes[3].errorbar(
    [position for position, _ in maldroid_valid],
    [float(row['macro_f1']) for _, row in maldroid_valid],
    yerr=[float(row['macro_f1_ci95']) for _, row in maldroid_valid],
    color='#DD8452',
    marker='o',
    markersize=3.5,
    linewidth=1.2,
    capsize=2,
)
axes[3].set_title('(d) MalDroid at 50%', fontsize=8)
axes[3].set_ylabel('Macro F1')

for axis in axes:
    axis.set_xticks(x, tick_labels, rotation=27, ha='right')
    axis.grid(axis='y', alpha=0.22, linewidth=0.6)

handles, labels = axes[0].get_legend_handles_labels()
fig.legend(handles, labels, loc='upper center', ncol=2, frameon=False, bbox_to_anchor=(0.5, 1.01))
fig.subplots_adjust(left=0.075, right=0.995, bottom=0.31, top=0.76, wspace=0.55)
fig.savefig(OUTPUT, bbox_inches='tight')
plt.close(fig)
print(OUTPUT)
