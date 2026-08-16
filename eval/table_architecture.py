#!/usr/bin/env python3
import csv
from pathlib import Path


HERE = Path(__file__).resolve().parent
DATA = HERE / 'data' / 'architecture.csv'
OUTPUT = HERE / 'tables' / 'architecture.tex'

with DATA.open(encoding='utf-8', newline='') as handle:
    rows = list(csv.DictReader(handle))

datasets = [('ddos', 'DDoS'), ('maldroid', 'MalDroid'), ('darknet', 'Darknet'), ('doh', 'DoH')]
architectures = ['X+X', 'L+X', 'X+L', 'L+L']
lines = [
    r'\begin{table}[t]',
    r'    \centering',
    r'    \caption{The table compares macro F1 across local and shared learners. Values are means over five splits. Bold marks the largest mean for each dataset.}',
    r'    \label{tab:eval-architecture}',
    r'    \footnotesize',
    r'    \setlength{\tabcolsep}{2.8pt}',
    r'    \begin{tabular}{@{}lrrrr@{}}',
    r'        \toprule',
    r'        Dataset & \makecell{XGB\\$\to$XGB} & \makecell{LGBM\\$\to$XGB} & \makecell{XGB\\$\to$LGBM} & \makecell{LGBM\\$\to$LGBM} \\',
    r'        \midrule',
]

for dataset, label in datasets:
    dataset_rows = {row['architecture']: row for row in rows if row['dataset'] == dataset}
    best = max(float(dataset_rows[architecture]['macro_f1']) for architecture in architectures)
    values = []
    for architecture in architectures:
        value = float(dataset_rows[architecture]['macro_f1'])
        text = '{:.3f}'.format(value)
        if value == best:
            text = r'\textbf{' + text + '}'
        values.append(text)
    lines.append('        {} & {} \\\\'.format(label, ' & '.join(values)))

lines.extend(
    [
        r'        \bottomrule',
        r'    \end{tabular}',
        r'\end{table}',
    ]
)
OUTPUT.write_text('\n'.join(lines) + '\n', encoding='utf-8')
print(OUTPUT)
