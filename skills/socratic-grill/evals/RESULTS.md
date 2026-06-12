# 评测记录

> 规矩：动 SKILL.md 的提问策略，必须跑 `evals/evals.json` 全量评测并在此追加记录；
> 汇总数字用 `scripts/report_evals.py` 生成，不要用 skill-creator 自带的
> aggregate_benchmark（它与 benchmark.json 结构不匹配，会产出 0% 零值假报告）。

## 2026-06-09 · iteration-2 全量评测

- 执行模型：claude-sonnet-4-6，9 个 eval × 2 配置 × 1 次运行
- 产物目录：`../socratic-grill-workspace/iteration-2/`（每个 eval 的 response.md 与 grading.json 可逐条对账）

| 配置 | 通过/总数 | 通过率 |
|---|---|---|
| with_skill（当时版本） | 48/49 | 98.0% |
| old_skill（上一轮版本） | 47/49 | 95.9% |

with_skill 唯一未通过项：`full-rollout-prelaunch` —— 追问未指向「小」这个量词背后的判断依据，而是直接问了回滚流程。

## 2026-06-09 · iteration-3 定向复测

针对上述失败项，SKILL.md 新增「模糊量词优先追问」规则（见 Question priority 末段）后复测：

| 配置 | 通过/总数 |
|---|---|
| with_skill | 6/6 ✅ |
| old_skill | 5/6 |

复测产物：`../socratic-grill-workspace/iteration-3/full-rollout-prelaunch/`。
该轮 with_skill 实际输出已收录为 [examples/prelaunch-full-rollout.md](../examples/prelaunch-full-rollout.md)。

## 已知缺口（下一轮评测应补）

- **缺 no-skill 裸模型基线**：现有对照组是旧版 skill，只能证明增量改进，不能直接证明"装 vs 不装"的差距。
- **runs_per_configuration = 1**：无方差数据，单次运行的通过率有运气成分。
- 触发评测 `../socratic-grill-workspace/trigger_eval.json`（16 条，10 正 6 负）尚未跑出留档结果。
