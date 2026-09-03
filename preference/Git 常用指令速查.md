# Git 常用指令速查

## 1. 查看状态

```bash
git status
```

查看当前分支、修改、暂存和未跟踪文件。

```bash
git status --short
```

简洁查看状态。

常见标记：

```text
M  已修改
A  已暂存
?? 未跟踪
D  已删除
```

---

## 2. 查看提交记录

```bash
git log
```

查看详细提交记录。

```bash
git log --oneline
```

简洁查看提交记录。

```bash
git log --oneline --graph --all
```

查看所有分支的提交关系图。

---

## 3. 添加和提交

添加全部修改：

```bash
git add .
```

添加指定文件：

```bash
git add 文件名
```

提交：

```bash
git commit -m "提交说明"
```

常用完整流程：

```bash
git add .
git status --short
git commit -m "提交说明"
```

---

## 4. 查看分支

查看本地分支：

```bash
git branch
```

查看本地和远程分支：

```bash
git branch -a
```

查看分支跟踪关系：

```bash
git branch -vv
```

当前分支前面会有：

```text
*
```

---

## 5. 创建和切换分支

创建新分支：

```bash
git branch 分支名
```

切换分支：

```bash
git switch 分支名
```

创建并切换：

```bash
git switch -c 分支名
```

例如：

```bash
git switch -c docs-review
```

从远程分支创建本地分支：

```bash
git switch -c 本地分支名 --track 远程名/远程分支名
```

例如：

```bash
git switch -c yangran-main --track yangran/main
```

---

## 6. 删除分支

删除本地分支：

```bash
git branch -d 分支名
```

强制删除本地分支：

```bash
git branch -D 分支名
```

删除远程分支：

```bash
git push origin --delete 分支名
```

不能删除当前所在分支，需要先切换：

```bash
git switch main
git branch -d 分支名
```

---

## 7. 查看远程仓库

```bash
git remote -v
```

查看远程仓库名称和地址。

常见远程名：

```text
origin    自己默认的远程仓库
upstream  原始项目仓库
yangran   自己添加的其他人的仓库
```

添加远程仓库：

```bash
git remote add 远程名 仓库地址
```

例如：

```bash
git remote add yangran https://github.com/yangran12/DianJiXZ.git
```

删除远程仓库别名：

```bash
git remote remove 远程名
```

例如：

```bash
git remote remove DianJiXZ
```

这只删除本地远程别名，不会删除 GitHub 仓库。

---

## 8. 获取远程更新

获取远程提交记录，但不修改当前文件：

```bash
git fetch
```

获取指定远程：

```bash
git fetch origin
```

获取其他人的仓库：

```bash
git fetch yangran
```

`fetch` 只更新 Git 记录，不直接修改工作区。

---

## 9. 拉取远程代码

```bash
git pull
```

等价于：

```bash
git fetch
git merge
```

拉取指定远程分支：

```bash
git pull origin main
```

更推荐保持提交线整洁：

```bash
git pull --rebase origin main
```

---

## 10. 推送代码

推送当前分支：

```bash
git push
```

第一次推送新分支：

```bash
git push -u origin 分支名
```

推送 main：

```bash
git push origin main
```

强制推送，谨慎使用：

```bash
git push --force-with-lease
```

不要轻易使用：

```bash
git push --force
```

---

## 11. 合并分支

先切换到接收代码的分支：

```bash
git switch main
```

再合并其他分支：

```bash
git merge 分支名
```

例如：

```bash
git switch main
git merge docs-review
```

意思是把 `docs-review` 合并进 `main`。

---

## 12. Cherry-pick：搬运某个提交

把某一个提交复制到当前分支：

```bash
git cherry-pick 提交哈希
```

例如：

```bash
git switch main
git cherry-pick abc1234
```

适合：

```text
错误提交到了其他分支
只想把其中一个提交搬到 main
```

出现冲突后：

```bash
git add .
git cherry-pick --continue
```

取消：

```bash
git cherry-pick --abort
```

---

## 13. 撤销工作区修改

撤销某个文件的未暂存修改：

```bash
git restore 文件名
```

撤销全部未暂存修改：

```bash
git restore .
```

危险：修改会直接丢失。

---

## 14. 取消暂存

已经执行了：

```bash
git add .
```

但还没有提交，可以取消暂存：

```bash
git restore --staged 文件名
```

取消全部暂存：

```bash
git restore --staged .
```

文件修改仍然保留。

---

## 15. 撤销提交

### 撤销最近一次提交，但保留修改

```bash
git reset --soft HEAD~1
```

提交取消，但文件仍在暂存区。

### 撤销最近一次提交，保留文件修改

```bash
git reset HEAD~1
```

提交取消，修改保留在工作区。

### 删除最近一次提交和修改

```bash
git reset --hard HEAD~1
```

危险：提交和文件修改都会消失。

### 撤销已经推送的提交

```bash
git revert 提交哈希
```

`revert` 会新建一个反向提交，更适合共享分支。

---

## 16. 暂存当前修改

临时保存未提交修改：

```bash
git stash
```

查看暂存列表：

```bash
git stash list
```

恢复最近一次暂存：

```bash
git stash pop
```

恢复但不删除暂存：

```bash
git stash apply
```

---

## 17. 查看代码差异

查看未暂存修改：

```bash
git diff
```

查看已暂存修改：

```bash
git diff --staged
```

查看两个分支差异：

```bash
git diff main..分支名
```

---

## 18. 解决冲突

发生冲突后：

```bash
git status
```

手动修改冲突文件，然后：

```bash
git add .
git commit
```

如果是 rebase：

```bash
git add .
git rebase --continue
```

取消 rebase：

```bash
git rebase --abort
```

取消 merge：

```bash
git merge --abort
```

---

## 19. 常用安全工作流

开发新功能：

```bash
git switch main
git pull --rebase origin main
git switch -c feature-name
```

完成后：

```bash
git add .
git commit -m "完成某功能"
git push -u origin feature-name
```

然后在 GitHub 创建 Pull Request。

---

## 20. main 更新后同步到自己的分支

```bash
git switch main
git pull --rebase origin main
git switch 自己的分支
git rebase main
```

出现冲突：

```bash
git add .
git rebase --continue
```

---

## 21. 误提交到错误分支

先找提交哈希：

```bash
git log --oneline
```

把提交搬到 main：

```bash
git switch main
git pull --rebase origin main
git cherry-pick 提交哈希
git push origin main
```

再回错误分支撤销。

未推送：

```bash
git switch 错误分支
git reset --hard HEAD~1
```

已推送：

```bash
git switch 错误分支
git revert 提交哈希
git push
```

---

## 22. origin/main 是什么

```text
origin       远程仓库名
main         分支名
origin/main  本地保存的远程 main 状态
```

通常：

```bash
git switch main
```

切换的是本地 `main`。

```bash
git fetch origin
```

会更新本地记录中的 `origin/main`。

---

## 23. 最常用的一组指令

```bash
git status
git branch -a
git branch -vv
git log --oneline --graph --all

git switch main
git switch -c 分支名

git add .
git commit -m "提交说明"

git fetch origin
git pull --rebase origin main
git push origin main

git merge 分支名
git cherry-pick 提交哈希

git restore .
git restore --staged .
git reset --soft HEAD~1
git revert 提交哈希

git remote -v
```

---

## 24. 操作前先检查

执行危险操作前，先运行：

```bash
git status
git branch -vv
git log --oneline -5
```

危险指令：

```bash
git reset --hard
git branch -D
git push --force
git clean -fd
```

不确定时优先不要执行。