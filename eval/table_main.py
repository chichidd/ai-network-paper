#!/usr/bin/env python3
import csv
from pathlib import Path


HERE = Path(__file__).resolve().parent
DATA = HERE / 'data' / 'main.csv'
OUTPUT = HERE / 'tables' / 'main.tex'

with DATA.open(encoding='utf-8', newline='') as handle:
    rows = list(csv.DictReader(handle))

names = {
    'all_encoders': 'Full detector pool',
    'random_budget': 'Random selection',
    'pointwise_utility': 'Individual utility ranking',
    'unified_brcc': r'\textbf{\Fname}',
}
datasets = ['ddos', 'maldroid', 'darknet', 'doh']
lines = [
    r'\begin{table*}[t]',
    r'    \centering',
    r'    \caption{Macro F1 at the 50\% selection-cost budget; random selection and individual utility ranking receive the same budget, the full detector pool is an unconstrained reference, and entries report means and 95\% Student $t$ confidence intervals over five repeated splits.}',
    r'    \label{tab:eval-main-results}',
    r'    \small',
    r'    \setlength{\tabcolsep}{4.5pt}',
    r'    \begin{tabular}{@{}lrrrr@{}}',
    r'        \toprule',
    r'        Method & DDoS & MalDroid & Darknet & DoH \\',
    r'        \midrule',
]

for row in rows:
    values = [
        '$' + '{:.4f}\\pm{:.4f}$'.format(float(row[dataset]), float(row[dataset + '_ci95']))
        for dataset in datasets
    ]
    lines.append('        {} & {} \\\\'.format(names[row['method']], ' & '.join(values)))

lines.extend(
    [
        r'        \bottomrule',
        r'    \end{tabular}',
        r'\end{table*}',
    ]
)
OUTPUT.write_text('\n'.join(lines) + '\n', encoding='utf-8')
print(OUTPUT)
