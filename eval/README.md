# Evaluation 图表编辑目录

这个目录只保存论文 Evaluation 正文正在使用的四张图和四张表。正式实验结果保持在 `unified-brcc/results/` 中，不在这里修改。`data/` 保存从已验证结果中抽出的紧凑快照，脚本读取这些小表后直接生成论文文件。

## 对应关系

| 正文结果 | 代码 | 数据 | 输出 | 对应问题 |
| --- | --- | --- | --- | --- |
| 预算与检测质量 | `fig_budget.py` | `data/budget.csv` | `../figures/eval_budget_utility.pdf` | RQ1 |
| 客户端标签异构性 | `fig_heterogeneity.py` | `data/heterogeneity.csv` | `../figures/eval_heterogeneity.pdf` | RQ2 |
| 分数随机化与检测质量 | `fig_privacy.py` | `data/privacy.csv` | `../figures/eval_privacy_utility.pdf` | RQ4 |
| 求解时间与部署规模 | `fig_scaling.py` | `data/scaling.csv` | `../figures/eval_solver_scaling.pdf` | RQ5 |
| 数据集规模 | `table_datasets.py` | `data/datasets.csv` | `tables/datasets.tex` | 实验设置 |
| 主要检测结果 | `table_main.py` | `data/main.csv` | `tables/main.tex` | RQ1 |
| 学习器架构 | `table_architecture.py` | `data/architecture.csv` | `tables/architecture.tex` | RQ3 |
| 运行与通信成本 | `table_cost.py` | `data/cost.csv` | `tables/cost.tex` | RQ5 |

## 使用方法

进入本目录后，直接运行需要修改的脚本。例如：

```bash
cd ai-network-paper/eval
../../unified-brcc/.venv/bin/python fig_budget.py
../../unified-brcc/.venv/bin/python table_main.py
```

每个绘图脚本都按“读取 CSV、设置样式、绘图、保存 PDF”的顺序从上到下执行，没有自定义绘图函数，也不依赖旧的多层渲染器。四张图只输出 Matplotlib PDF，并固定使用 TrueType 字体。每个表格脚本同样从上到下生成一份 LaTeX 文件，`new-eval.tex` 会通过 `\input{eval/tables/...}` 直接读取这些表格。

## 数据来源

| 紧凑数据 | 已验证结果来源 |
| --- | --- |
| `datasets.csv` | 样本量和特征数来自 `unified-brcc/results/unified-brcc-e0-e7-paper-v1/table2_datasets.csv`；评估类别数来自正式混淆矩阵的 `labels` |
| `main.csv`、`budget.csv` | `unified-brcc/results/unified-brcc-e0-e7-paper-v1/table8_budget_sensitivity.csv` |
| `heterogeneity.csv` | `table9_partition_feasibility.csv` 与 `table9_controlled_heterogeneity.csv` |
| `architecture.csv` | `table4_architectures_long.csv` 的 Macro F1 列 |
| `privacy.csv` | `unified-brcc/results/unified-brcc-dp-sensitivity-v1/paper/dp_sensitivity_summary.csv` |
| `scaling.csv` | `unified-brcc/results/unified-brcc-e0-e7-paper-v1/table12_solver_audit.csv` |
| `cost.csv` | `table5_runtime.csv`、`table6_logical_communication_compact.csv` 与 `table4_unified_methods.csv` |

这些 CSV 是论文展示快照，不是新的实验结果。修改图的颜色、字号或布局时只改对应脚本。只有实验结果本身发生变化时，才更新 `data/` 中的数值。

DDoS 的原始数据统计表记录 14 个原始类别编号，而正式密封测试混淆矩阵实际包含 13 个评估标签，其中一个标签没有出现在客户端训练类集合中。因此，`datasets.csv` 和正文表使用 13 个“评估类别”，而不是直接复制原始类别编号总数。
