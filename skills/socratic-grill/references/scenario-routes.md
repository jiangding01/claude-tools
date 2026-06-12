# Scenario Routes

Use this file as a routing map, not a fixed questionnaire.

For every user problem, identify the closest scenario and ask only the highest-leverage next question.

| 场景 | 核心目标 | 推荐追问路线 | 代表性问题 | 收敛标准 |
|---|---|---|---|---|
| 需求澄清 | 确认到底解决谁的什么问题 | 用户 → 痛点 → 价值 → 范围 → 非目标 → 指标 → 验收 → 边界 | 这个需求解决的是谁的什么问题？ | 用户、痛点、范围、非目标、指标、验收、边界清楚 |
| 方案评审 | 发现漏洞、缺失、分歧和风险 | 目标 → 假设 → 边界 → 上下游 → ROI → 风险 → 验收 → 行动 | 这个方案最核心的判断前提是什么？ | 目标、假设、风险、影响面、验收、行动项清楚 |
| 技术设计 / 架构 | 判断技术路径是否合理、可维护、可回滚 | 业务目标 → 约束 → 边界 → 数据 → 状态 → 接口 → 失败 → 观测 → 回滚 | 这个设计中最难反悔的决策是什么？ | 目标、边界、数据、状态、失败模式、观测、回滚清楚 |
| QA / 测试策略 | 明确测试重点、风险覆盖和上线信心 | 改动范围 → 主链路 → 高风险 → 回归 → 边界 → 数据 → 验收 → 上线观察 | 哪个场景失败代价最高？ | 范围、主链路、高风险、回归、验收、观察、兜底清楚 |
| Bug / 故障排查 | 区分现象、影响面、根因、修复和验证 | 现象 → 复现 → 影响面 → 时间线 → 变更 → 假设 → 证据 → 修复 → 防复发 | 最近一次相关变更是什么？ | 现象、影响面、根因证据、修复、验证、防复发清楚 |
| 上线前检查 | 判断是否具备上线条件 | 范围 → 影响面 → 灰度 → 回滚 → 降级 → 监控 → Owner → 止损 | 什么指标触发暂停或回滚？ | 范围、灰度、回滚、降级、监控、Owner、止损条件清楚 |
| 数据分析 / 指标归因 | 避免拍脑袋归因，找到可行动结论 | 指标定义 → 口径 → 事实 → 分群 → 时间线 → 变量 → 假设 → 证据 → 行动 | 当前归因是数据支持，还是经验判断？ | 口径、事实、分群、归因、证据、行动、验证指标清楚 |
| 业务运营策略 | 明确运营目标、对象、机制、成本和验证方式 | 目标 → 人群 → 动机 → 触达 → 转化 → 成本 → ROI → 执行 → 复盘 | 这次运营动作具体优化哪个指标？ | 目标、人群、动机、转化、成本、ROI、复盘清楚 |
| 流程优化 / SOP / 自动化 | 找到流程断点、低效节点和自动化机会 | 触发 → 输入 → 输出 → 流程 → Owner → 卡点 → 异常 → 标准化 → 自动化 → 指标 | 这个流程从哪个明确事件开始？ | 起点、输入输出、Owner、卡点、异常、自动化边界、指标清楚 |
| 跨团队协作 / 分歧对齐 | 识别分歧类型，推动共识落地 | 表象 → 分歧类型 → 各方目标 → 约束 → 不可妥协点 → 决策人 → 标准 → 沉淀 | 你们真正的分歧是目标不同，还是风险判断不同？ | 分歧类型、诉求、决策标准、决策人、行动、沉淀清楚 |
| 项目复盘 | 从结果中提炼可复用经验 | 目标 → 结果 → 差异 → 正确判断 → 错误假设 → 过程问题 → 机制问题 → 改进 | 哪个关键假设被证明是错的？ | 事实、差异、假设、根因、经验、行动、责任人清楚 |
| 文档评审 | 判断文档是否清楚、完整、可执行 | 读者 → 目标 → 读者动作 → 结论 → 证据 → 结构 → 缺失 → 矛盾 → 可执行性 | 这份文档读完后，读者应该做出什么动作？ | 读者、目标、结论、证据、缺失信息、可执行动作清楚 |
| 个人职场决策 | 分清价值、风险、机会成本和下一步 | 选择 → 目标 → 约束 → 机会成本 → 风险 → 可逆性 → 长期收益 → 最小验证 → 下一步 | 这个选择主要是在追求上限，还是降低风险？ | 目标、约束、成本、风险、可逆性、下一步清楚 |

## Active incident mode

When the user describes an **active production incident** — error rate is live, alerts are firing, users are affected right now — apply these adjustments to the Bug/故障排查 route:

- Skip the 核心命题对齐 framing header. Go straight to assumption identification and the question.
- In "为什么重要", reflect the time cost: every minute of wrong-direction investigation extends the blast radius.
- Prioritize questions that eliminate root-cause hypotheses quickly over questions that are structurally complete.
- Do not ask about "防复发" until the incident is mitigated.

Signals that this is an active incident (not a post-mortem): user mentions error rate / alert / on-call / user complaints happening now, or asks "我们该怎么排查".

## Scenario selection rules

- If the user provides a PRD, spec, proposal, or plan: prefer 方案评审 or 文档评审.
- If the user talks about users, value, MVP, or acceptance: prefer 需求澄清.
- If the user talks about architecture, code, interfaces, state, data, or implementation: prefer 技术设计 / 架构.
- If the user talks about tests, coverage, regression, or release confidence: prefer QA / 测试策略.
- If the user talks about symptoms, errors, logs, or production issues: prefer Bug / 故障排查.
- If the user talks about launch, release, grayscale, rollback, or monitoring: prefer 上线前检查.
- If the user talks about metrics, funnel, attribution, or conversion: prefer 数据分析 / 指标归因.
- If the user talks about operations, campaigns, conversion, users, or execution: prefer 业务运营策略.
- If the user talks about repeated manual work, SOP, handoff, or automation: prefer 流程优化.
- If the user talks about disagreement or cross-team conflict: prefer 跨团队协作.
- If the user talks about what went well or wrong: prefer 项目复盘.
- If the user asks whether they personally should do something: prefer 个人职场决策.
