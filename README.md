# MUM Workflows

面向全国大学生数学建模竞赛（CUMCM）、美赛（MCM/ICM）、电工杯等赛事的轻量协作参考仓库。它提供赛前准备、赛中接力、项目模板与可复用 Skill；不提供赛题答案，也不替代当届官方规则。

## 先从这里开始

1. 想系统学习：从 [教程路线](tutorials/README.md) 开始。
2. 想马上动手：选择 [练习区](practice/README.md) 的一个练习。
3. 准备开赛：复制 [项目骨架](templates/project-starter/)，完成 [赛前准备](workflows/preparation.md)。
4. 已经开赛：按 [72 小时赛中工作流](workflows/competition-72h.md) 建任务卡、决策日志和可复现入口。
5. 使用 Agent 或需要标准协作步骤：从 [Skill 库](skills/README.md) 选择对应的 `MCM-` Skill。

> 赛题、原始附件、个人信息和未公开的比赛结果不应进入公开仓库。参赛期间请使用**私有**竞赛仓库，并以当届官方规则为准。

## 仓库地图

```text
preference/   参考资料：赛事、方法、工具与外部参考资料索引
tutorials/    教程：按顺序阅读的学习材料
practice/     练习区：可实际完成并自检的任务
workflows/    使用手册：赛前、赛中、交接与终检操作卡
templates/    可复制到私有竞赛仓库的项目与论文骨架
skills/       四个 `MCM-` 开头、可被 Agent/人工复用的协作 Skill
docs/         本仓库维护说明、演进计划与维护者资料
.github/      本仓库维护使用的 Issue 与 Pull Request 模板
```

## 不同目录怎么用

| 你要做什么 | 先去哪里 | 完成标志 |
| --- | --- | --- |
| 查找方法、工具或赛事参考入口 | `preference/` | 知道资料来源、适用边界与官方复核要求 |
| 从零学习协作与建模项目组织 | `tutorials/` | 能说清每一步的目的，并完成对应练习 |
| 亲手练 Git、图表或论文装配 | `practice/` | 有可检查的交付物和自检记录 |
| 真实比赛中组织团队工作 | `workflows/` + `templates/` | 私有项目能被队友接手和复现 |
| 增补或维护这个参考仓库 | `docs/` + `CONTRIBUTING.md` | 提交内容可公开、可验证、可维护 |

## 最小协作约定

- `main` 只保留已验证、可交接的内容；每个任务在独立分支完成后以 PR 合并。
- 每个子问题先建任务卡，再写代码；结论必须能追溯到数据、参数、命令和图表。
- 原始数据与外部资料默认本地保存；提交前先检查是否含敏感信息、二进制大文件和 LaTeX 编译产物。
- 规则、格式和 AI 使用要求会随年份变化。模板只提供核对入口，不宣称永久合规。

详见 [团队协作约定](workflows/team-collaboration.md) 与 [提交前检查清单](workflows/pre-submit-checklist.md)。

## 设计边界

本仓库刻意保持轻量：不内置复杂评分器、在线任务系统或特定题目的答案。若需要更完整的阶段化 Agent 流程，可研究 [mathmodel-skill](https://github.com/handsomeZR-netizen/mathmodel-skill)；其中的共享决策日志与竞赛差异分层是本仓库的参考来源，但本仓库的文档与模板独立维护。

## 开源与使用

本仓库以 [MIT License](LICENSE) 发布。你可以使用、复制、修改和分发仓库中的内容，但须保留许可证与版权声明。第三方资料、当届官方规则、赛题附件及其各自使用条款不因本许可证而改变。
