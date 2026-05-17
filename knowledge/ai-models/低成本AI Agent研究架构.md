---
tags: [量化知识库, 量化知识库/AI模型, 量化知识库/研究方法]
aliases: [低成本AI Agent研究架构, Codex优先的Agent研究架构]
created: 2026-05-17
updated: 2026-05-17
---

# 低成本 AI Agent 研究架构

关联：[[AI模型知识]]、[[研究方法知识]]、[[量化因子研究入口地图]]

## 来源

- [Using Codex with your ChatGPT plan](https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan)：Codex 可随 ChatGPT 计划使用，具体额度受计划限制。
- [Managing Billing Settings on ChatGPT Web and Platform](https://help.openai.com/en/articles/9039756)：ChatGPT 订阅和 API Platform 是分开的计费系统。
- [How can I move my ChatGPT subscription to the API?](https://help.openai.com/en/articles/8156019-is-api-usage-included-in-chatgpt-subscriptions-even-if-i-have-a-paid-chatgpt-account)：API 使用按 token 计费，不能简单等同于 ChatGPT 订阅。
- [Ollama OpenAI compatibility](https://docs.ollama.com/openai)：Ollama 可在本地暴露 OpenAI 兼容接口，适合本地模型实验。
- [vLLM OpenAI-compatible server](https://docs.vllm.ai/en/latest/serving/openai_compatible_server.html)：vLLM 可作为 OpenAI 兼容服务端，但更偏 GPU/服务化部署。
- [LiteLLM docs](https://docs.litellm.ai/)：LiteLLM 可作为多模型/多供应商的 OpenAI 兼容代理层。
- [Microsoft Agent Framework overview](https://learn.microsoft.com/en-us/agent-framework/overview/)：明确区分 agent 与 workflow，并提醒能用函数解决就不应强行 agent 化。
- [LangGraph overview](https://docs.langchain.com/oss/python/langgraph/overview)：适合长流程、状态和可观测性较强的 agent/workflow 编排。

## 问题

真正的问题不是“哪个 agent 框架最强”，而是：

> 在预算有限、已经订阅 Codex、暂时不想额外购买大量 API key 的情况下，如何把 AI agent 用成可持续的研究能力？

这里需要拆开三个层次：

1. **框架成本**：LangGraph、Pydantic AI、LlamaIndex、CrewAI、LiteLLM、Ollama 等多数是开源或可免费本地安装的。
2. **模型调用成本**：真正持续花钱的通常是 OpenAI、Google、Anthropic、Azure 等云模型 API。
3. **运行环境成本**：本地模型不花 API 钱，但消耗本机 CPU/GPU/内存，效果和速度也受硬件限制。

所以低成本路线不是“找一个免费 agent 框架”，而是：

> 用 Codex 做主要高质量推理与代码操作；用本地开源模型做便宜的批处理、格式检查、初稿和低风险辅助；把关键评测、门禁和执行交给确定性代码。

## 机制

### 1. Codex 本身应当先被当作 agent workbench

在当前阶段，最现实的主力不是另起一个 LangGraph/CrewAI 服务，而是把 Codex 用好：

- 让 Codex 读本地仓库、论文、笔记和产物。
- 通过本地 skill 固化研究流程。
- 用 shell、脚本、测试、Markdown 档案承载确定性步骤。
- 把每次研究沉淀成 Obsidian 笔记、handoff memo 或后续 automation prompt。

这相当于把 Codex 当成“交互式总控 agent”，而不是马上自己搭一个 agent 平台。

### 2. 框架不是先选，先选控制边界

低成本 agent 系统的核心边界：

| 层 | 推荐做法 | 原因 |
|---|---|---|
| 研究方向判断 | Codex + 笔记 + 外部资料 | 需要强推理和上下文理解，优先用已订阅能力 |
| 论文/资料初筛 | Codex 为主，本地模型可做批量摘要 | 本地模型适合低风险粗处理 |
| 候选因子规格 | 结构化 Markdown/JSON/YAML | 不急着引入框架，先稳定 schema |
| 质量门禁 | Python 确定性规则 | 字段白名单、PIT、未来函数不能靠 LLM 自觉 |
| 数值评测 | Python runner | IC、RankIC、成本、容量必须可复现 |
| 结果复盘 | Codex + reviewer prompt | 适合 LLM 做解释、反驳、下一代变异 |
| 归档 | Obsidian + JSON artifact | 低成本、可迁移、可审计 |

### 3. 本地模型只放在低风险环节

如果以后要减少 API 依赖，可以先从 Ollama 开始：

```text
Ollama local model
  -> OpenAI-compatible localhost endpoint
  -> LiteLLM optional routing layer
  -> small local scripts / prototype agent calls
```

适合本地模型的任务：

- 批量摘要论文段落。
- 把非结构化文字转成初版 JSON。
- 检查 frontmatter、标签、引用、格式。
- 对已完成评测报告做低成本初评。
- 生成多个候选名称、假设表述或反方问题。

不建议本地小模型承担：

- 最终研究方向判断。
- 高风险代码修改。
- 未来函数审查的最终结论。
- 实盘/交易相关动作。
- 复杂数学、长上下文论文综合的唯一判断来源。

## 框架判断

### 当前优先级

1. **Codex + Obsidian + 本地脚本**：现在就能用，最少新增成本。
2. **Ollama**：如果要实验“免费模型调用”，先用它做本地模型入口。
3. **LiteLLM**：当你同时接 Codex/API、本地 Ollama、其他模型时，再作为统一代理层。
4. **Pydantic / Pydantic AI**：当候选输出需要强 schema 和测试时再引入。
5. **LangGraph**：当流程已经重复、状态复杂、需要自动循环和人工门禁时再引入。
6. **LlamaIndex**：当资料库/RAG 成为主要瓶颈时再引入。
7. **CrewAI / Google ADK / Microsoft Agent Framework**：先学习概念，不作为当前主线依赖。

### 为什么不急着上完整 agent 框架

完整框架容易带来三种成本：

- **模型生态成本**：示例默认绑定某家模型或云服务。
- **工程维护成本**：状态、回调、trace、部署、权限都要维护。
- **幻觉成本**：多个 agent 互相讨论，看起来热闹，但不一定提高可验证研究质量。

如果一个流程可以用 Markdown 模板、Python 函数和 Codex review 完成，就先不要框架化。只有出现稳定重复流程后，再抽象成 workflow。

## 与 CogAlpha 的关系

CogAlpha 对我们最有价值的是方法论：

```text
代码化 alpha
  -> 多视角候选生成
  -> quality gate
  -> fitness evaluation
  -> adaptive generation
  -> thinking evolution / lineage
```

低成本落地时，不应该先复刻“21 个 autonomous agents”，而应该先复刻“研究控制面”：

```text
Codex 主控
  -> 研究方向笔记
  -> 候选 schema
  -> deterministic quality gate
  -> deterministic evaluation runner
  -> Codex reviewer
  -> Obsidian archive
  -> 下一轮 mutation queue
```

也就是说，CogAlpha 的 agent 不一定先是框架里的 `Agent()` 对象。它们可以先是：

- 角色说明。
- 候选模板。
- 审查清单。
- 输出 schema。
- 失败原因 taxonomy。
- 下一轮变异规则。

当这些对象稳定后，再决定是否把它们迁移到 LangGraph/Pydantic AI/LlamaIndex。

## 可行性路线

### Phase 0：Codex-only

目标：不买新 API，不上新服务。

产物：

- `agent_roles.md`：研究总监、资料检索、候选设计、风险审查、证据审查。
- `candidate_schema.md`：候选因子必须包含的问题、机制、字段、PIT 假设、评测 horizon。
- `review_checklist.md`：未来函数、字段可得性、容量、过拟合、重复性。
- Obsidian 主题笔记和 handoff memo。

判断标准：

- 每次研究能留下清楚的假设、证据、失败原因和下一步。
- 不是只完成“流程阶段”，而是能看到某个指标或判断维度是否改善。

### Phase 1：Local model sidecar

目标：把低风险、重复、便宜的工作交给本地模型。

工具候选：

- Ollama：本地模型入口。
- LiteLLM：统一 OpenAI 兼容调用接口。
- 小脚本：批量摘要、格式校验、JSON 初稿。

判断标准：

- 本地模型输出必须经过 Codex 或确定性规则复核。
- 本地模型不能直接写入生产仓库或触发交易动作。

### Phase 2：Typed agent outputs

目标：让 agent 输出变成可测试对象。

工具候选：

- Pydantic。
- Pydantic AI。
- JSON Schema。

判断标准：

- 候选因子、审查结论、mutation plan 都能被 schema 校验。
- 不合格输出直接 reject，不靠人工猜测。

### Phase 3：Workflow engine

目标：只有当研究循环稳定后才引入。

工具候选：

- LangGraph：状态、分支、循环、人工门禁。
- LlamaIndex Workflows：资料/RAG 密集型流程。

判断标准：

- workflow 必须减少重复劳动，而不是增加维护负担。
- 每个节点有明确输入、输出、失败条件和人工接管点。

## 边界

- ChatGPT/Codex 订阅和 API Platform 计费是分开的；不能假设订阅等于无限 API 调用。
- 开源框架免费，不代表模型推理免费。
- 本地模型免费，不代表效果足够好。
- 多 agent 不是目标，稳定研究闭环才是目标。
- 当前阶段优先把知识、流程和评价标准沉淀在 `vortex_docs`，不要直接在这里实现生产研究 runner。

## 下一步

1. 先写一份 `CogAlpha 低成本 Agent 角色与输出契约`，把 6 个核心角色定义清楚。
2. 用一篇已有论文或资料跑一次 Codex-only 流程，不引入新框架。
3. 如果批量摘要或格式整理开始耗费时间，再试 Ollama + 本地模型。
4. 如果候选输出开始稳定，再引入 Pydantic schema。
5. 如果流程每周反复运行，才考虑 LangGraph 或 LlamaIndex workflow。
