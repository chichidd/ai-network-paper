#!/usr/bin/env python3
import csv
from pathlib import Path

import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt


HERE = Path(__file__).resolve().parent
DATA = HERE / 'data' / 'budget.csv'
OUTPUT = HERE.parent / 'figures' / 'eval_budget_utility.pdf'

with DATA.open(encoding='utf-8', newline='') as handle:
    rows = list(csv.DictReader(handle))

plt.rcParams.update(
    {
        'font.family': 'DejaVu Sans',
        'font.size': 7.5,
        'axes.spines.top': False,
        'axes.spines.right': False,
        'pdf.fonttype': 42,
        'ps.fonttype': 42,
    }
)

datasets = [('ddos', 'DDoS'), ('maldroid', 'MalDroid'), ('darknet', 'Darknet'), ('doh', 'DoH')]
methods = [
    ('unified_brcc', 'SiloStitch', '#3B6FB6', 'o'),
    ('pointwise_utility', 'Individual utility', '#DD8452', 's'),
    ('random_budget', 'Random', '#55A868', '^'),
]

fig, axes = plt.subplots(1, 4, figsize=(7.16, 2.18), sharex=True)

for axis, (dataset, title) in zip(axes, datasets):
    dataset_rows = [row for row in rows if row['dataset'] == dataset]
    for method, label, color, marker in methods:
        points = sorted(
            [row for row in dataset_rows if row['method'] == method],
            key=lambda row: float(row['budget']),
        )
        axis.errorbar(
            [float(row['budget']) for row in points],
            [float(row['macro_f1']) for row in points],
            yerr=[float(row['ci95']) for row in points],
            color=color,
            marker=marker,
            markersize=3.6,
            linewidth=1.25,
            capsize=2,
            label=label,
        )

    full = next(row for row in dataset_rows if row['method'] == 'all_encoders')
    axis.errorbar(
        [100],
        [float(full['macro_f1'])],
        yerr=[float(full['ci95'])],
        color='#333333',
        marker='*',
        markersize=7,
        linewidth=0,
        capsize=2,
        label='Full pool',
    )
    axis.set_title(title, fontsize=8.5, pad=3)
    axis.set_xticks([25, 50, 75, 100])
    axis.grid(axis='y', alpha=0.22, linewidth=0.6)
    axis.margins(y=0.18)

axes[0].set_ylabel('Macro F1')
fig.supxlabel('Selection cost budget (%)', fontsize=7.5, y=0.02)
handles, labels = axes[0].get_legend_handles_labels()
fig.legend(handles, labels, loc='upper center', ncol=4, frameon=False, bbox_to_anchor=(0.5, 1.01))
fig.subplots_adjust(left=0.075, right=0.995, bottom=0.23, top=0.76, wspace=0.34)
fig.savefig(OUTPUT, bbox_inches='tight')
plt.close(fig)
print(OUTPUT)
