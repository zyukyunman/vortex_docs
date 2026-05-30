---
tags: [量化知识库, 量化知识库/研究方法, 量化知识库/论文]
aliases: [Slope Strength散户外推路径因子线索, SlopeStrength散户外推, 路径平滑外推因子]
created: 2026-05-19
updated: 2026-05-19
source_type: 论文
status: 实现候选
---

# Slope Strength 散户外推路径因子线索

## 一句话结论

这条线索把“过去收益”拆成趋势斜率和路径平滑度，适合作为 A 股路径类因子的最小可证伪 seed，但当前只基于摘要级核验，不能写成确定结论。

## 来源

- Chad Schmerling, *Slope, Strength, and Retail Extrapolation*, SSRN, 2026-05-07.
- 链接：https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6731259
- 本地交接：[[2026-05-19 因子研究线索交接 人工重启]]

## 核心机制

论文摘要的核心机制是：投资者形成收益预期时可能不仅看累计涨跌幅，还看路径是否平滑、是否容易被视觉外推。用滚动窗口对累计收益做时间趋势回归，可以提取 trend slope 和 trend strength。平滑上升路径与 noisy downward trend 之间的价差，可能反映散户外推和信息渐进扩散。

## 证据与边界

摘要称作者在 CRSP 1962-2025 样本上发现该路径特征在 Fama-French + momentum 之外仍有 alpha，并且效果集中在低机构持股股票，同时与 PEAD 更强有关。

边界：

- 当前只做摘要级核验，没有深读完整 PDF。
- 海外 CRSP、低机构持股和美股 PEAD 机制不能直接等同于 A 股。
- A 股涨跌停、停牌、ST、复权和小盘流动性会改变路径形态。

## 可迁移点

- 第一轮只迁移可观测路径特征：rolling OLS slope、R2/strength、趋势残差波动。
- 必须和普通 momentum、短反、低波、PRV、amount crowding、moneyflow、industry、size 做负对照。
- 如果可观测字段不足以区分“散户外推”与“低波趋势”，应把结论降级为路径类技术特征，而不是行为因子。

## 失败风险

- 参数挖掘：窗口、平滑度定义和方向容易被后验调优。
- 重复因子：可能只是 momentum + lowvol 的轻微变体。
- PIT 风险：复权、滚动标准化、停牌填充和行业成分若处理不当会泄漏。

## 下一步

- 已在 rolling multi-round 模式下选为当前活跃 seed，来源交给 `vortex_quant` 只读消费。
- 最小反证：20/60 日滚动 slope + strength，评测 5d/20d/60d RankIC、ICIR、positive_rate、long-short，并做完整 controls 后 residual IC。

## 关联链接

- [[量化研究候选议题池]]
- [[量化因子研究入口地图]]
- [[DRIF日收益信息因子线索]]
- [[行业拥挤补跌风险线索]]
