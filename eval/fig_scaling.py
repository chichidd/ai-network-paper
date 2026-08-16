#!/usr/bin/env python3
import csv
from pathlib import Path

import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


HERE = Path(__file__).resolve().parent
DATA = HERE / 'data' / 'scaling.csv'
OUTPUT = HERE.parent / 'figures' / 'eval_solver_scaling.pdf'

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

fig, axes = plt.subplots(1, 2, figsize=(6.92, 1.87))

candidate_rows = [row for row in rows if row['sweep'] == 'candidates']
candidate_x = np.asarray([int(row['x']) for row in candidate_rows])
candidate_y = np.asarray([float(row['median_seconds']) for row in candidate_rows])
candidate_high = np.asarray([float(row['p95_seconds']) for row in candidate_rows]) - candidate_y
axes[0].errorbar(
    candidate_x,
    candidate_y,
    yerr=np.vstack([np.zeros_like(candidate_high), candidate_high]),
    color='#3B6FB6',
    marker='o',
    markersize=3.8,
    linewidth=1.25,
    capsize=2,
)
axes[0].set_title('(a) More candidate models', fontsize=8.5)
axes[0].set_xlabel('Candidate models')
axes[0].set_xticks(candidate_x)

class_rows = [row for row in rows if row['sweep'] == 'classes']
class_x = np.asarray([int(row['x']) for row in class_rows])
class_y = np.asarray([float(row['median_seconds']) for row in class_rows])
class_high = np.asarray([float(row['p95_seconds']) for row in class_rows]) - class_y
axes[1].errorbar(
    class_x,
    class_y,
    yerr=np.vstack([np.zeros_like(class_high), class_high]),
    color='#DD8452',
    marker='s',
    markersize=3.8,
    linewidth=1.25,
    capsize=2,
)
axes[1].set_title('(b) More attack classes', fontsize=8.5)
axes[1].set_xlabel('Attack classes')
axes[1].set_xticks(class_x)

for axis in axes:
    axis.set_yscale('log')
    axis.grid(axis='y', which='both', alpha=0.22, linewidth=0.6)
axes[0].set_ylabel('Selection time (s, log scale)')

fig.subplots_adjust(left=0.105, right=0.995, bottom=0.28, top=0.79, wspace=0.28)
fig.savefig(OUTPUT, bbox_inches='tight')
plt.close(fig)
print(OUTPUT)
