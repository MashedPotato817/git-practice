# Git 练习仓库

通过「选提示词 → AI 生图 → 提交 → PR」的完整流程，练习 Git 协作：fork / clone、分支、规范 commit、push、Pull Request。

仓库地址：<https://github.com/MashedPotato817/git-practice>

## 练习目标

- 学会获取远程仓库（fork 与 collaborator 两种方式）
- 掌握分支的创建与切换
- 按 `.agents/skills/git-workflow/SKILL.md` 的规范提交
- push 到自己的分支并发起 Pull Request

## 前置要求

- 本机安装 Git
- 注册 GitHub 账号
- 任一 AI 生图模型（如 GPT-Image2），用于生成任务图片

## 第一步：获取仓库（二选一）

**路径 A：fork**（没有本仓库写权限时使用）

1. 打开仓库页面，点击右上角 `Fork`，将仓库复制到自己账号下
2. 克隆你自己的 fork：

   ```bash
   git clone https://github.com/<你的用户名>/git-practice.git
   ```

**路径 B：共同创作者**（已被邀请为 collaborator）

```bash
git clone https://github.com/MashedPotato817/git-practice.git
```

## 第二步：创建工作分支

```bash
git checkout -b feat/images-<练习者id>
```

分支命名等约定统一见 [assets/image-prompts](assets/image-prompts/README.md)。

## 第三步：领取任务并生成图片

前往 [assets/image-prompts](assets/image-prompts/README.md) 选择一个任务，复制提示词生成图片，并按其中的约定命名、放入 `assets/images/`。

## 第四步：提交

提交信息遵循 `.agents/skills/git-workflow/SKILL.md`，规范详解见 [preference/Git 提交信息规范](preference/Git%20提交信息规范.md)，常用命令见 [preference/Git 常用指令速查](preference/Git%20常用指令速查.md)。

```bash
git add .
git commit -m "feat(images): 添加系统框图-张三"
```

开发过程中可以随时提交保存进度，不要求一次到位。

## 第五步：推送并提交 PR

```bash
git push -u origin feat/images-<练习者id>
```

- fork 者推送到自己的 fork；collaborator 推送到本仓库的同名分支
- **禁止直接 push main**，一切通过 PR 合并
- 在 GitHub 页面发起 Pull Request，标题按 commit 规范书写，描述中附图片预览；PR 模板会引导你完成自检

## 维护者审核

维护者确认暂定稳定后，使用 "Create a merge commit" 合并，并将合并消息编辑为规范格式（与 PR 标题一致）。

## FAQ

**Q：main 有更新，如何同步到我的分支？**

```bash
git checkout main && git pull   # fork 者先在 GitHub 页面点击 Sync fork
git checkout feat/images-<练习者id>
git merge main -m "chore(branch): 同步main最新改动"
```

**Q：push 被拒（rejected）？**

通常是远程分支已有新提交，先执行 `git pull --rebase` 或按上一条同步 main 后再推。

**Q：遇到合并冲突怎么办？**

打开冲突文件，理解双方意图后手动合并，`git add` 后再 commit，不要机械丢弃任何一方的内容。

## 成果一览

完成练习后，把自己的成果加进下表（这也是 PR 的一部分）：

| 练习者 id | 任务 | 图片链接 | 日期 |
|-----------|------|----------|------|
| （等待第一位练习者） | | | |
