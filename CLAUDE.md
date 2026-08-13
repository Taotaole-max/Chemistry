# Chemistry

化学计算与仿真。机器学习 + 材料科学方向的个人项目仓库。

## 沟通偏好

用中文回答。文档和代码注释也用中文。

## 项目结构

- `data/` — 输入/输出数据
- `src/` — 计算/仿真脚本
- `projects/` — 独立小项目，每个自带 README 和 requirements
  - `bandgap-prediction-rf/` — 随机森林预测材料带隙
- `docs/AI_FOR_CHEMISTRY_GUIDE.md` — AI for Chemistry 学习路线图

## 跨会话记忆

本地 Claude Code 和云端会话**不共享对话历史**，git 仓库是唯一的记忆通道。
做完一件有结论的事就用 `memory` skill 把结论写回仓库并推送——没推送等于没记住。

下面两个文件会随本文件自动加载：

@.claude/memory/decisions.md
@.claude/memory/gotchas.md

时间线在 [`.claude/memory/journal.md`](.claude/memory/journal.md)，按需读最上面几条（倒序），不要整篇读。

## 约定

- 依赖装在虚拟环境里，新依赖同时写进对应的 `requirements.txt`
- `.env` 存 API key，永远不提交
- 云端会话推到 `claude/*` 功能分支；记忆类改动要尽快合并到 `main`，否则其他会话看不见
