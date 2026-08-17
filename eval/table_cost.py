#!/usr/bin/env python3
import csv
from pathlib import Path


HERE = Path(__file__).resolve().parent
DATA = HERE / 'data' / 'cost.csv'
OUTPUT = HERE / 'tables' / 'cost.tex'

with DATA.open(encoding='utf-8', newline='') as handle:
    rows = list(csv.DictReader(handle))

names = {'ddos': 'DDoS', 'maldroid': 'MalDroid', 'darknet': 'Darknet', 'doh': 'DoH'}
lines = [
    r'\begin{table*}[t]',
    r'    \centering',
    r'    \caption{We report the time required to evaluate every selection rule and budget on one machine, together with total logical communication at the 50\% selection cost budget. Times are means over five splits. The final column reports the macro F1 loss relative to the full detector pool.}',
    r'    \label{tab:eval-system-cost}',
    r'    \small',
    r'    \setlength{\tabcolsep}{4.2pt}',
    r'    \begin{tabular}{@{}lrlrrrr@{}}',
    r'        \toprule',
    r'        Dataset & \makecell{Runtime\\(min)} & Dominant stage & \makecell{Full pool\\(MiB)} & \makecell{\Fname\\(MiB)} & \makecell{Communication\\saved} & \makecell{Macro F1\\loss} \\',
    r'        \midrule',
]

for row in rows:
    dominant = '{} ({:.1f}\\%)'.format(row['dominant_stage'], float(row['dominant_percent']))
    lines.append(
        '        {} & {:.2f} & {} & {:,.2f} & {:,.2f} & {:.1f}\\% & {:.4f} \\\\'.format(
            names[row['dataset']],
            float(row['replay_minutes']),
            dominant,
            float(row['full_mib']),
            float(row['selected_mib']),
            float(row['saved_percent']),
            float(row['macro_f1_loss']),
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
