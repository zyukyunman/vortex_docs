---
tags: [量化知识库, 量化知识库/AI模型, 量化知识库/研究方法]
aliases: [FactorEngine失败经验库因子挖掘线索, FactorEngine因子挖掘, 失败经验库因子挖掘]
created: 2026-05-19
updated: 2026-05-19
source_type: 论文
status: 种子
---

# FactorEngine 失败经验库因子挖掘线索

## 一句话结论

FactorEngine 对 Vortex 的主要启发是把 LLM 因子挖掘拆成可审计程序、失败经验库和有界搜索，而不是让模型无界生成表达式。

## 来源

- Qinhong Lin 等，*FactorEngine: A Program-level Knowledge-Infused Factor Mining Framework for Quantitative Investment*, arXiv, 2026-03-17.
- 链接：https://arxiv.org/abs/2603.16365

## 核心机制

论文摘要描述的框架把因子表示为程序级代码，并拆分三件事：

- logic revision 与 parameter optimization 分离；
- LLM-guided directional search 与 Bayesian hyperparameter search 分离；
- LLM 调用与本地计算分离。

它还强调从非结构化金融报告中抽取候选逻辑，并用经验知识库记录失败轨迹，支持后续 refinement。

## 证据与边界

摘要称 FactorEngine 在真实 OHLCV 数据回测中相对 baseline 提升 IC/ICIR、RankIC/ICIR 和组合指标。

边界：

- 当前只做摘要级核验，没有复现代码或数据。
- 论文回测结果不能作为 Vortex 本地因子有效性证据。
- 对 Vortex 更有价值的是控制面方法，而不是直接复用论文框架。

## 可迁移点

- 把每个关闭路径的 no-reopen rules 写进失败经验库。
- 在 candidate design 中区分“逻辑修订”和“参数优化”，避免窗口/阈值无界挖参。
- 每轮 mutation 必须声明 parent_factor、primary_objective、guardrails、mutation_budget 和 rejected_pool。

## 失败风险

- LLM 看到评测结果后围绕 scorecard 调参，形成隐性过拟合。
- 经验库混入绑定本地 runner 的结论后，被复制到上游 `vortex_docs`。
- 因子程序表达力变强后，quality gate 反而更难发现未来函数和重复路径。

## 下一步

- 先作为 `skill_candidate` 保留。
- 最小反证：选 DRIF 或 weak substitution 这种已关闭研究线，检查失败经验库能否提前阻断 no-reopen 变体；不能减少重复候选时不沉淀 skill。

## 关联链接

- [[AI模型知识]]
- [[量化研究自动化任务设计]]
- [[WorldQuant BRAIN Alpha训练纪律来源卡]]
