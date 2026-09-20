# MUM Workflows

面向全国大学生数学建模竞赛（CUMCM）、美赛（MCM/ICM）、电工杯等赛事的轻量协作参考仓库。它提供赛前准备、赛中接力、项目模板与可复用 Skill；不提供赛题答案，也不替代当届官方规则。

## 先从这里开始

1. 想系统学习：从 [教程路线](tutorials/README.md) 开始。
2. 想马上动手：选择 [练习区](practice/README.md) 的一个练习。
3. 准备开赛：复制 [项目骨架](templates/project-starter/)，完成 [赛前准备](workflows/preparation.md)。
4. 已经开赛：按 [72 小时赛中工作流](workflows/competition-72h.md) 建任务卡、决策日志和可复现入口。
5. 使用 AI 协作：阅读 [竞赛项目工作流 Skill](skills/contest-project-workflow/SKILL.md)，或复制到你的 Agent Skill 目录。

> 赛题、原始附件、个人信息和未公开的比赛结果不应进入公开仓库。参赛期间请使用**私有**竞赛仓库，并以当届官方规则为准。

## 仓库地图

```text
skills/       可复用的 Agent/人工协作 Skill
workflows/    赛前与赛中的操作流程
templates/    可 fork/复制的竞赛项目骨架与论文骨架
library/      赛事、方法、工具与外部参考资料索引
tutorials/    从入门到终检的连续教程
practice/     Git 协作、小型建模和论文装配练习
docs/         协作原则、角色边界、检查清单与维护说明
.github/      Issue 与 Pull Request 模板
```

## 最小协作约定

- `main` 只保留已验证、可交接的内容；每个任务在独立分支完成后以 PR 合并。
- 每个子问题先建任务卡，再写代码；结论必须能追溯到数据、参数、命令和图表。
- 原始数据与外部资料默认本地保存；提交前先检查是否含敏感信息、二进制大文件和 LaTeX 编译产物。
- 规则、格式和 AI 使用要求会随年份变化。模板只提供核对入口，不宣称永久合规。

详见 [协作约定](docs/collaboration.md) 与 [提交前检查清单](docs/pre-submit-checklist.md)。

## 设计边界

本仓库刻意保持轻量：不内置复杂评分器、在线任务系统或特定题目的答案。若需要更完整的阶段化 Agent 流程，可研究 [mathmodel-skill](https://github.com/handsomeZR-netizen/mathmodel-skill)；其中的共享决策日志与竞赛差异分层是本仓库的参考来源，但本仓库的文档与模板独立维护。

## 开源与使用

当前仓库尚未指定开源许可证。在许可证明确前，请先取得维护者许可再复制、再发布或将内容用于其他仓库。
