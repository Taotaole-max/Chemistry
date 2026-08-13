# 坑与环境怪癖

> 下次还会踩的坑、走不通的路、环境的特殊之处。
> **失败的尝试和成功的方案一样值钱**——它能挡住未来的重复劳动。

## 云端会话的容器是临时的

会话结束容器就被回收，**没有 commit + push 的东西全部消失**。云端会话里做完一段有价值的工作就立刻提交，不要攒着。

## 云端会话默认推到功能分支

云端会话被指定推到 `claude/*` 功能分支，不直接推 `main`。后果是：写在功能分支上的记忆，其他新会话（从 `main` 全新 clone）看不到。记忆类改动要尽快合并到 `main`。

## Materials Project 需要 API key

`projects/bandgap-prediction-rf/` 要连 Materials Project 取数据，key 放在 `.env`（参考同目录的 `.env.example`）。`.env` 已在 `.gitignore` 里，**不要提交**。云端会话没有这个 key，跑不了真实取数流程。
