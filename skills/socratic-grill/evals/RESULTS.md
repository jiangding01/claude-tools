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

## 2026-06-12 · 触发精度（trigger precision）首次留档

- 方法：3 次独立子 Agent dry-run（每次都是"全新会话拿到 description 后判断是否调用该 skill"，不知晓修改历史），不依赖真实 Skill 调度器。
- 测试集：[evals/trigger_eval.json](trigger_eval.json)（20 条，10 正 10 负，从 `../socratic-grill-workspace/trigger_eval.json` 迁入）。

| 配置 | 通过/总数 | 通过率 |
|---|---|---|
| 改写前 description（强制二选一） | 20/20 | 100% |
| 改写后 description（强制二选一） | 20/20 | 100% |

二者在 20 条强制二选一测试中都是满分，改写**未带来二元结果的翻转**。但触发动机是更早一轮 5 条「会/不会/不确定」三选项边界复测——改写前，类似 `给我列一下 MySQL 分库分表的最佳实践` 这类请求会被判为"不确定"（description 里"pre-launch risk check / PRD review"等正触发场景词与"a ready-made checklist of best practices"负触发存在字面重叠）。

针对 SKILL.md description 负触发段落新增「即使话题与上述场景重叠，只要用户要的是通用最佳实践清单/模板而非审视自己的具体方案，就不触发」的明确规则 + 两个中文示例短语后，三选项复测（5 条边界 case）：

| Case | 改写后判断 |
|---|---|
| "给我列一下 MySQL 分库分表的最佳实践" | 不会（直接命中新增示例短语） |
| "帮我列一个上线前检查清单的最佳实践，要全面一点" | 不会（清晰判定，不再"不确定"） |
| "上线前检查清单有哪些？" | 不会 |
| "我们这个方案上线前，按最佳实践应该检查哪些风险点？" | **不确定**（"我们这个方案"指向正触发，"按最佳实践"指向负触发，规则仍冲突） |
| "帮我过一遍这个方案的上线检查清单，看看我们漏了什么" | 会 |

4/5 边界 case 从模糊变清晰，验证门通过（无回归 + 解决已记录歧义），改动保留。剩余 1 条（"我们这个方案…按最佳实践应该检查哪些风险点"）留作已知边界——它同时引用"自己的方案"和"最佳实践"框架，语义上更接近应该触发（针对自己方案的检查），但 description 目前没有给到足够权重判断这点，留给下一轮处理。

## 已知缺口（下一轮评测应补）

- **缺 no-skill 裸模型基线**：现有对照组是旧版 skill，只能证明增量改进，不能直接证明"装 vs 不装"的差距。
- **runs_per_configuration = 1**：无方差数据，单次运行的通过率有运气成分。
- **触发精度边界 case**：`"我们这个方案上线前，按最佳实践应该检查哪些风险点？"` 这类"自己的方案 + 最佳实践框架"的混合表述仍判定为"不确定"，倾向应该触发（针对具体方案的检查），description 需要进一步明确"自己的方案"这一信号的优先级。
