#!/usr/bin/env python3
import csv
from pathlib import Path

import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


HERE = Path(__file__).resolve().parent
DATA = HERE / 'data' / 'privacy.csv'
OUTPUT = HERE.parent / 'figures' / 'eval_privacy_utility.pdf'

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

epsilon_order = ['no_noise', '50', '20', '10', '7', '5', '3', '1']
tick_labels = ['None', '50', '20', '10', '7', '5', '3', '1']
policies = [
    ('unified_selected_50', '50% budget', '#3B6FB6', 'o'),
    ('all_candidates', 'Full pool', '#DD8452', 's'),
]
x = np.arange(len(epsilon_order))

fig, axes = plt.subplots(2, 1, figsize=(3.28, 2.78), sharex=True)

for policy, label, color, marker in policies:
    points = [next(row for row in rows if row['policy'] == policy and row['epsilon'] == epsilon) for epsilon in epsilon_order]
    axes[0].errorbar(
        x,
        [float(row['macro_f1']) for row in points],
        yerr=[float(row['macro_f1_ci95']) for row in points],
        color=color,
        marker=marker,
        markersize=3.4,
        linewidth=1.2,
        capsize=2,
        label=label,
    )
    axes[1].errorbar(
        x,
        [float(row['attack_leakage']) for row in points],
        yerr=[float(row['attack_leakage_ci95']) for row in points],
        color=color,
        marker=marker,
        markersize=3.4,
        linewidth=1.2,
        capsize=2,
        label=label,
    )

axes[0].set_title('(a) Detection quality', fontsize=8)
axes[0].set_ylabel('Macro F1')
axes[1].set_title('(b) Attacks among benign predictions', fontsize=8)
axes[1].set_ylabel('Attack leakage')
axes[1].set_xticks(x, tick_labels)
axes[1].set_xlabel('Per block ε (stronger noise →)')

for axis in axes:
    axis.grid(axis='y', alpha=0.22, linewidth=0.6)

handles, labels = axes[0].get_legend_handles_labels()
fig.legend(handles, labels, loc='upper center', ncol=2, frameon=False, bbox_to_anchor=(0.5, 1.01))
fig.subplots_adjust(left=0.19, right=0.98, bottom=0.18, top=0.83, hspace=0.72)
fig.savefig(OUTPUT, bbox_inches='tight')
plt.close(fig)
print(OUTPUT)
