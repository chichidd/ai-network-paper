#!/usr/bin/env python3
import csv
from pathlib import Path


HERE = Path(__file__).resolve().parent
DATA = HERE / 'data' / 'datasets.csv'
OUTPUT = HERE / 'tables' / 'datasets.tex'

with DATA.open(encoding='utf-8', newline='') as handle:
    rows = list(csv.DictReader(handle))

names = {'ddos': 'DDoS', 'maldroid': 'MalDroid', 'darknet': 'Darknet', 'doh': 'DoH'}
lines = [
    r'\begin{table*}[t]',
    r'    \centering',
    r'    \caption{Scale of the four evaluation tasks; each task uses 66 clients and one candidate detector per client, evaluated classes count labels in the sealed test set, and DDoS includes one test class absent from client training.}',
    r'    \label{tab:eval-datasets}',
    r'    \small',
    r'    \begin{tabular}{lrrrr}',
    r'        \toprule',
    r'        Dataset & Training samples & Test samples & Features & Evaluated classes \\',
    r'        \midrule',
]

for row in rows:
    lines.append(
        '        {} & {:,} & {:,} & {:,} & {:,} \\\\'.format(
            names[row['dataset']],
            int(row['training_samples']),
            int(row['test_samples']),
            int(row['features']),
            int(row['evaluated_classes']),
        )
    )

lines.extend(
    [
        r'        \bottomrule',
        r'    \end{tabular}',
        r'\end{table*}',
    ]
)
OUTPUT.write_text('\n'.join(lines) + '\n', encoding='utf-8')
print(OUTPUT)
