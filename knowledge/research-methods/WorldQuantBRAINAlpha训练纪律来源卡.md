---
tags: [量化知识库, 量化知识库/研究方法, 量化知识库/资料]
aliases: [WorldQuant BRAIN Alpha训练纪律来源卡, WorldQuant BRAIN训练纪律, BRAIN Alpha纪律]
created: 2026-05-19
updated: 2026-05-19
source_type: 文章
status: 种子
---

# WorldQuant BRAIN Alpha 训练纪律来源卡

## 一句话结论

WorldQuant BRAIN 适合作为 alpha 表达训练、算子约束和质量门禁纪律的来源，不适合作为直接搬运 alpha 或直接证明 A 股因子有效的来源。

## 来源

- WorldQuant BRAIN / International Quant Championship 2026：https://www.worldquant.com/brain/iqc/
- WorldQuant BRAIN Learn to Quant alpha examples：https://worldquantbrain.com/alpha-examples
- 本地入口：[[量化因子研究入口地图]]

## 核心机制

BRAIN 的公开信息强调通过平台数据集、算子和 alpha 表达式创建可提交的信号。它对 Vortex 的价值主要在研究纪律：

- alpha 表达必须受字段和算子约束；
- 候选需要经过提交评测或等价质量检查；
- 重复、过拟合和不可提交表达应尽早淘汰；
- 训练流程可以帮助研究者形成“先定义表达边界，再看证据”的习惯。

## 证据与边界

公开 IQC 页面列出 2026 webinar 节奏，覆盖 BRAIN 介绍、基本面/模型数据、价量数据、D0 alpha 和新数据集等主题。公开 alpha examples 页面提供按数据类别拆解 alpha 的学习材料。

边界：

- 平台数据、提交评分、私有字段和评测口径不透明。
- 平台内 alpha 涉及知识产权和合规边界，不能复制。
- BRAIN 结果不能作为 A 股本地因子有效性证据。

## 可迁移点

- 借鉴表达式纪律、字段白名单、算子白名单和重复度检查。
- 把公开 Alpha101 复现作为 duplicate guardrail，不作为 alpha 结论。
- 在候选设计阶段明确“不搬运平台 alpha，只迁移研究纪律”。

## 失败风险

- 把训练题或平台 alpha 当作本地研究成果。
- 把平台分数当成 A 股数据证据。
- 忽略 BRAIN 与 Vortex 数据字段、可见时间、交易制度和成本模型差异。

## 下一步

- 将其作为 `source_card` 保留。
- 若后续提炼 skill，只写“表达纪律和边界检查”，不写平台内 alpha。

## 关联链接

- [[量化研究候选议题池]]
- [[量化因子研究入口地图]]
- [[SlopeStrength散户外推路径因子线索]]
