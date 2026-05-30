---
tags: [量化知识库, 量化知识库/研究方法, 量化知识库/论文]
aliases: [Transient Statistical Factors 风险模型增强来源卡, 风险模型短时统计因子增强来源卡]
created: 2026-05-20
updated: 2026-05-20
source_type: 论文/方法论
---

# Transient Statistical Factors 风险模型增强来源卡

## 来源

- 标题：Enhancing a Risk Model by Adding Transient Statistical Factors
- 作者：Alexandros E. Tzikas, Emmanuel J. Candès, Trevor Hastie, Stephen P. Boyd, Mykel J. Kochenderfer, Ronald N. Kahn
- 提交：2026-05-13
- 链接：https://arxiv.org/abs/2605.12977

## 核心想法（只记可迁移部分）

- 在既有 factor risk model 基础上，增加“短时有效”的统计因子（transient factors），用 half-life 加权的似然目标去拟合缺失数据也可适配的收益序列结构。
- 对 Vortex 的意义：这更像“风险模型增强/门禁工具箱”，而不是“挖 alpha 因子”。

## A 股落地的最小问题集

- 数据：仅使用收益序列 + 已有风格/行业暴露是否足够？停牌/退市/新股缺失如何处理？
- 点时：half-life/窗口定义是否严格点时（不能用未来波动校准窗口长度）？
- 评测：只比较风险预测质量与组合权重稳定性，不引入收益目标避免泄漏。
