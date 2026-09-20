# Skill 库

本目录的 Skill 是给 Agent 或熟练协作者使用的“工作约定”，不是新人教程，也不是自动解题器。所有公开 Skill 都以 `MCM-` 开头，名称直接说明它解决的任务。

## 最小用法

1. 先根据任务选择一个 Skill，再阅读其 `SKILL.md`，确认输入、产物和人工确认点。
2. 使用 Agent 时，按该工具的官方 Skill 安装方式复制整个 Skill 文件夹；手动协作时，直接把其中步骤作为任务清单。
3. Skill 的输出仍需由队员核对数据、题意、结果和当届规则。

| Skill | 何时使用 | 人工确认 |
| --- | --- | --- |
| [`MCM-Git-Workflow`](MCM-Git-Workflow/SKILL.md) | 分支、提交、PR、合并、同步或推送 | 合并与远端影响 |
| [`MCM-Project-Workflow`](MCM-Project-Workflow/SKILL.md) | 拆题、数据检查、建模、复现或交接 | 题意、假设、模型与结果 |
| [`MCM-Paper-Writing`](MCM-Paper-Writing/SKILL.md) | 写摘要、模型、结果、评价或终检论文 | 结论强度、披露与最终提交 |
| [`MCM-Visualization`](MCM-Visualization/SKILL.md) | 绘制或检查示意图、Python/Origin 数值图 | 数据来源、图型与结论 |

## 与工作流的区别

- `workflows/` 面向全体队员，是比赛中可以直接照做的操作卡。
- `skills/` 面向 Agent 或熟练协作者，用于在具体任务中组织判断、产物和人工确认。
