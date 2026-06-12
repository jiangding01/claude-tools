# Role Lenses

Use role lenses to pressure-test the same problem from different workplace functions.

| 角色 | 关注点 | 典型追问 |
|---|---|---|
| SRE / 运维 | 稳定性、可用性、容量规划、监控覆盖、告警阈值、故障隔离、回滚成本、事故影响面 | 这个变更如果凌晨触发告警，值班同学能在 5 分钟内定位根因吗？ |
| PM | 用户价值、需求真实性、MVP、范围、优先级、成功指标、体验、验收 | 如果用户只能感知到一个变化，这个变化应该是什么？ |
| Dev | 技术可行性、系统边界、数据模型、状态流转、接口依赖、异常处理、可维护性、回滚成本 | 这个方案里哪个技术决策未来最难反悔？ |
| QA | 测试范围、主链路、异常流、回归风险、数据构造、验收口径、上线信心 | 如果只能重点测三类场景，哪一类漏测后的损失最大？ |
| Ops | 业务目标、执行路径、用户触达、转化效果、运营成本、SOP、落地阻力 | 这个动作是一次性运营动作，还是能沉淀成长期机制？ |
| Manager / Owner | 资源投入、优先级、决策权、时间线、风险承担、跨团队依赖、责任边界 | 如果资源只能支持一半范围，你会砍掉哪部分而不破坏核心目标？ |
| Data | 指标定义、统计口径、分群、漏斗、归因、对照组、数据质量、实验设计 | 这个结论如果要变成业务动作，最少还缺哪一条数据证据？ |
| PMO | 里程碑、交付风险、跨团队依赖、Owner 明确性、变更影响、沟通机制、预算/资源投入、项目关闭条件 | 这个项目里有哪个关键依赖方还没有明确 Owner 和交付时间节点？ |

## How to use role lenses

1. Identify the user's current perspective.
2. Identify the missing perspective.
3. Ask one question from the missing perspective.
4. Explain why that role would care.
5. Return to the main route after the risk or disagreement is clarified.

## Cross-functional disagreement types

- 术语分歧：同一个词含义不同
- 事实分歧：对现实情况的判断不同
- 目标分歧：优化目标不同
- 范围分歧：边界不同
- 优先级分歧：重要性排序不同
- 风险分歧：风险承受能力不同
- 成本分歧：对投入产出判断不同
- 证据分歧：证据标准不同
- 责任分歧：Owner 和边界不清
- 实现分歧：建设路径不同

## Disagreement template

```markdown
### ⚠️ 分歧定位

我看到这里可能不是单纯的方案分歧，而是 <分歧类型>。

你当前强调的是：<用户立场>
另一个可能视角是：<另一职能或另一方视角>

---

### 🔥 关键追问

问题：<只问一个能定位真实分歧的问题>

为什么重要：<说明如果分歧类型不清，会造成什么后果>

我的当前判断：<你对分歧本质的判断>
```
