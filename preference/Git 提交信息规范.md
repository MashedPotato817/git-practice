# Git Commit Message（提交信息规范）

## 基本格式

```bash
git commit -m "<type>: <description>"
```

示例：

```bash
git commit -m "feat: 新增数字识别功能"
git commit -m "fix: 修复串口通信异常"
git commit -m "docs: 更新 README"
```

---

## 常用 Type

| Type | 含义 | 示例 |
|------|------|------|
| `feat` | 新增功能（Feature） | `feat: 新增登录功能` |
| `fix` | 修复 Bug | `fix: 修复串口初始化失败` |
| `docs` | 文档修改 | `docs: 更新开发文档` |
| `refactor` | 重构（不新增功能、不修 Bug） | `refactor: 重构图像处理模块` |
| `perf` | 性能优化 | `perf: 优化模型推理速度` |
| `style` | 代码格式调整（不影响逻辑） | `style: 调整代码缩进` |
| `test` | 添加或修改测试 | `test: 增加串口单元测试` |
| `chore` | 构建、依赖、配置等杂项 | `chore: 更新依赖版本` |
| `build` | 构建系统修改 | `build: 修改 CMake 配置` |
| `ci` | CI/CD 配置修改 | `ci: 更新 GitHub Actions` |
| `revert` | 回滚提交 | `revert: 回滚上一版本修改` |

---

## 电赛项目示例

### 新功能

```bash
git commit -m "feat: 新增数字识别算法"
git commit -m "feat: 支持 K230 摄像头采集"
git commit -m "feat: 增加路径规划模块"
```

### Bug 修复

```bash
git commit -m "fix: 修复串口通信异常"
git commit -m "fix: 修正 PID 参数计算"
git commit -m "fix: 修复图像畸变导致识别失败"
```

### 文档

```bash
git commit -m "docs: 更新开发文档"
git commit -m "docs: 补充比赛报告"
git commit -m "docs: 完善 README"
```

### 重构

```bash
git commit -m "refactor: 重构图像处理流程"
git commit -m "refactor: 拆分通信模块"
```

### 配置

```bash
git commit -m "chore: 更新 .gitignore"
git commit -m "chore: 修改工程配置"
```

---

## 推荐原则

✅ 一次 Commit 做一件事

```text
feat: 新增数字识别
```

不要

```text
feat: 新增数字识别、修改文档、修 Bug、改 UI
```

---

## Description 编写建议

推荐使用：

- 新增……
- 支持……
- 修复……
- 更新……
- 重构……
- 优化……
- 删除……

例如：

```text
feat: 支持二维码识别
fix: 修复摄像头初始化失败
docs: 更新开发环境说明
refactor: 重构串口通信模块
perf: 优化目标检测速度
chore: 更新依赖版本
```

---

## 一个典型开发流程

```bash
git status

git add .

git commit -m "feat: 新增数字识别"

git push
```

---

## Conventional Commits（推荐规范）

```
<type>: <description>
```

例如：

```
feat: 新增登录功能
fix: 修复内存泄漏
docs: 更新 README
refactor: 重构通信模块
perf: 优化推理速度
test: 增加单元测试
style: 格式化代码
chore: 更新依赖
```

这是目前 GitHub、GitLab、Google、Angular、Vue、React 等大量开源项目广泛采用的提交规范。