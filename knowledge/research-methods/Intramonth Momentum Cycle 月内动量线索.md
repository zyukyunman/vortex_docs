---
tags: [量化知识库, 量化知识库/研究方法, 量化知识库/论文]
aliases: [Intramonth Momentum Cycle 月内动量线索, 月内动量周期, PreTOM momentum]
created: 2026-05-23
updated: 2026-05-23
source_type: 学术论文
status: 种子
---

# Intramonth Momentum Cycle 月内动量线索

## 来源

- [SSRN: The Intramonth Momentum Cycle](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6426026)
- 作者：Daniel Nathan、Matti Suominen、Joni Tasa。
- 版本：Posted 2026-03-23；Last revised 2026-05-13。

## 核心机制

论文把动量收益的一部分解释为月末现金需求和结算制度导致的市场管道效应：投资者在月末前需要 settled cash 时，更容易卖出 loser 股票，从而让动量 spread 在月内固定窗口集中出现。

## 证据与边界

摘要称美股 1980-2025 的动量收益集中在月末前 6 个交易日，并用 T+2 到 T+1 结算转换提供窗口平移识别，还在 19 个发达市场观察到类似 loser-driven 结构。

这不是 A 股结论。A 股股票交易、资金清算、公募申赎和投资者结构不同，本地只能把它作为 momentum/calendar gate 的候选机制，而不是直接搬成正向 alpha。

## 可迁移点

- 可观测字段猜想：交易日历、月末相对交易日、过去 12-1 或短期 momentum、loser/winner 分组、流动性、换手、指数回撤。
- 最小证伪：冻结论文窗口，比较窗口内外 loser/winner 的 5d/20d 表现差，不做窗口搜索。
- 适合角色：momentum 和 path-structure 因子的风险门禁或日历条件。

## 失败风险

- 本地若通过回看收益选择“最优月内窗口”，会直接变成数据窥探。
- A 股缺少可直接观测的月末现金需求和机构赎回压力字段。
- 如果只在小样本或特定年份成立，应关闭为 calendar anomaly，不进入策略链路。

## 下一步

交给 `vortex_quant` 时，先查重月末效应、短反、momentum、path_structure 和流动性路径；若重复或 loser-driven 证据不成立，直接关闭。

## 关联链接

- [[量化研究候选议题池]]
- [[SlopeStrength散户外推路径因子线索]]
- [[量化因子研究入口地图]]
