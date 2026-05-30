---
tags: [量化知识库, 量化知识库/研究方法, 量化知识库/论文]
aliases: [Cross-Market Alpha短周期价量因子迁移线索, Alpha191跨市场短周期价量线索]
created: 2026-05-25
updated: 2026-05-25
source_type: 论文
status: 种子
---

# Cross-Market Alpha短周期价量因子迁移线索

## 来源

- 论文：[Cross-Market Alpha: Testing Short-Term Trading Factors in the U.S. Market via Double-Selection LASSO](https://arxiv.org/abs/2601.06499)
- 作者：Jin Du, Alexander Walter, Maxim Ulrich
- 日期：2026-05-22；arXiv v2 于 2026-05-21 修订
- 关联：[[量化研究候选议题池]]、[[高频价格跳跃峰岭谷因子线索]]、[[滴水穿石成交量周期性因子线索]]、[[WorldQuant BRAIN Alpha训练纪律来源卡]]

## 核心机制

论文把国泰君安 Alpha191 这类 A 股短周期价量/微观结构信号当作“行为足迹库”，用 double-selection LASSO 在美股 S&P 500 上检验它们是否在传统基本面因子之外仍有解释力。其核心不是“照搬 Alpha191”，而是提出一个更高门槛：短周期价量信号必须在大量传统因子和同族价量因子控制后，仍能贡献非冗余风险溢价。

## 证据与边界

- 证据来自 S&P 500 2002-2022 样本，不是 A 股本地评测。
- 论文称从 168 个可用 Alpha191 信号中筛出 17 个显著信号，覆盖 OBV、价量相关、gap、Volume MACD、ATR、RSI、收益偏度等家族。
- DS-LASSO 提供的是高维筛选和控制框架，不等于每个幸存信号都有稳定、可交易、成本后可实现的 alpha。

## 可迁移点

- 可迁移为 `alpha191_short_term_behavioral_signal_guard`：先按信号家族做 archive lookup，再决定是否选少数父代进入质量门禁。
- 本地 A 股优先比较：PRV、价格跳跃峰岭谷、日内 range/bar shape、short reversal、lowvol、size、amount、turnover、moneyflow 和 industry。
- 研究价值在于“短周期价量家族的非冗余性审查”，不是全库挖掘。

## 失败风险

- Alpha191 表达式多且相关性强，极易多重检验。
- 如果直接全库搜索，会与现有 PRV、价格跳跃、成交量周期、短反、低波等路径重叠。
- VWAP、benchmark、成分、复权、停牌、涨跌停和窗口构造必须点时安全。
- LASSO 参数和筛选结果不能用未来收益回看调优。

## 下一步

只作为 guarded seed 写入资料交接包。若当前 active seed 关闭或归档，研究任务可以先做 archive lookup：从论文 17 个幸存信号所属家族中选择最多 2-3 个可解释父代，先判定与现有价量/微观结构档案是否重复；重复则关闭，不写 runner。

## 关联链接

- [[量化研究候选议题池]]
- [[高频价格跳跃峰岭谷因子线索]]
- [[滴水穿石成交量周期性因子线索]]
- [[WorldQuant BRAIN Alpha训练纪律来源卡]]
