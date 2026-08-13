# 会话日志

> 最新的在最上面。格式见 `.claude/skills/memory/SKILL.md`。
> 不记录代码 diff（git 已经记了），只记录发生了什么、学到了什么、下一步是什么。

## 2026-08-13 · 云端会话

**做了**：搭起跨会话记忆机制——`CLAUDE.md` 作为自动加载的索引，`.claude/memory/` 存明细，`.claude/skills/memory/` 是维护它的 skill。

**学到**：本地和云端会话之间不存在任何自动的上下文共享，git 仓库是唯一通道。

**下一步**：把这套东西合并到 `main`，否则本地会话看不到。

## 2026-08-10 ~ 08-13 · 早期工作（事后补记）

**做了**：初始化仓库结构；写了 `docs/AI_FOR_CHEMISTRY_GUIDE.md`（AI+化学入门路线图，含中文入门内容）；加了 `projects/bandgap-prediction-rf/`（Materials Project 数据 + matminer 特征 + 随机森林预测带隙）。

**学到**：用户偏好中文材料——指南后来专门补了更简单的中文机器学习入口。
