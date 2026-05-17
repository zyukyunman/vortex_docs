---
name: obsidian
description: Obsidian 知识库管理技能。用于在 vortex_docs 中创建、编辑、重组或链接 Markdown 笔记，覆盖 MOC 页面、wikilink、YAML frontmatter、标签、别名、图谱结构和断链校验。
---

# Obsidian 知识库管理

`vortex_docs` 是 Obsidian 优先的知识库。Markdown 笔记不只是文件，还应该能在图谱里被导航、被引用、被复用。

## 适用范围

用于这些位置下的笔记：

- `README.md`
- `docs/`
- `knowledge/`
- `library/`
- `materials/`
- `inbox/`

不要把 Obsidian frontmatter 强行加到 `.codex/skills/*/SKILL.md`；skill 文件本身已有独立 YAML 契约。

## Frontmatter

持久笔记使用：

```yaml
---
tags: [量化知识库, 量化知识库/<领域标签>]
aliases: [<主要 wikilink 名称>, <可选别名>]
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

规则：

- `aliases` 第一个值是标准 wikilink 目标。
- 编辑时保留已有 aliases。
- 有实质修改时更新 `updated`。
- 概念笔记优先使用稳定中文别名。

## 标签

基础标签：

- `量化知识库/索引`：MOC 和索引页。
- `量化知识库/流程`：仓库流程、工作规范。
- `量化知识库/资料`：原始资料索引。
- `量化知识库/书籍`：书籍阅读或策略提炼。
- `量化知识库/论文`：论文阅读。
- `量化知识库/量化系统`：量化系统、回测、MLOps、Harness。
- `量化知识库/资产配置`：资产配置、投资框架、组合管理。
- `量化知识库/AI模型`：AI 建模和金融机器学习。
- `量化知识库/研究方法`：研究方法论。
- `量化知识库/职业`：职业和面试材料。
- `量化知识库/归档`：历史版本、重复材料、低频参考。

## Wikilink

稳定知识关系用 wikilink：

```markdown
[[知识库结构总览]]
[[永久投资组合策略操作提炼]]
[[资产配置知识]]
```

本地 PDF、代码路径和外部网址用 Markdown 链接。

## MOC 规则

MOC 页面包含：

1. 一句话说明它回答什么问题。
2. 简短结构图或列表。
3. 使用 `[[wikilink]]` 的主题入口。
4. 下一步阅读或操作路线。

新增持久笔记时，更新最近的 MOC。

当前 MOC 层级：

```text
README.md
└── docs/README.md
    ├── knowledge/README.md
    ├── library/README.md
    └── materials/README.md
```

## 图谱卫生

- 避免孤立节点。
- 每篇持久笔记都应能从某个 MOC 到达。
- 优先中心辐射结构，避免所有文档互相乱连。
- 链接概念，不链接每一个重复词。

## 校验

批量编辑后运行：

```bash
python3 .codex/skills/obsidian/scripts/validate_wikilinks.py .
```

结束前修复未解析的 wikilink 或补 aliases。
