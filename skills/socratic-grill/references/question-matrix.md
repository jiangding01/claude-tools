# Question Matrix

Use one dimension at a time. Pick the dimension that most affects the current decision.

## 1. 概念澄清

Use when the user uses vague words like:

- 提升体验
- 提高效率
- 降低成本
- 更灵活
- 更稳定
- 更智能
- 更简单
- 更好用
- 标准化
- 平台化
- 自动化
- 高质量
- 可扩展
- 可维护

Template:

```markdown
### 🔍 术语澄清

你这里的「<术语>」会直接影响后续判断。

问题：在这个场景里，「<术语>」具体指什么可观察、可衡量或可验收的结果？

为什么重要：如果这个词不落到具体标准，后面很容易变成主观争论。

我的当前判断：这个词目前还停留在愿景层，尚不足以支撑方案评审。
```

## 2. 目标与成功标准

Use when goal, priority, or success is unclear.

Example:

```text
问题：这个需求上线后，哪个指标变化可以证明它是成功的？

为什么重要：没有成功标准，评审、开发、测试和复盘都会失去统一判断尺。
```

## 3. 前置假设

Use when the user presents an unverified premise as fact.

Template:

```markdown
### ⚠️ 假设识别

这里我会把「<判断>」先降级为假设，而不是事实。

问题：这个假设目前有什么证据支撑？

为什么重要：如果这个假设不成立，方案的核心价值可能会被削弱。

我的当前判断：在证据不足前，应该先设计低成本验证，而不是直接进入完整建设。
```

## 4. 证据与事实

Use when the evidence basis is unclear.

Example:

```text
问题：你判断这个问题值得做，依据是数据、用户反馈、业务方诉求，还是团队经验？

为什么重要：不同证据强度决定我们应该直接投入，还是先做小规模验证。
```

## 5. 边界与异常流

Use when the happy path works but edge cases are unclear.

Template:

```markdown
### 🧪 边界压测

我用一个异常场景压一下这个方案。

场景：<具体异常场景>

问题：在这个场景下，系统、流程或团队应该如何处理？

为什么重要：主流程跑通只能证明可演示，异常流闭环才证明可上线。

我的当前判断：当前方案对异常流的兜底还不够明确。
```

Common edge cases:

- 空数据
- 重复提交
- 权限不足
- 网络异常
- 第三方接口失败
- 并发冲突
- 数据延迟
- 状态不一致
- 历史数据兼容
- 资损风险
- 人工兜底

## 6. ROI 与机会成本

Use when cost is clear but value is vague.

Template:

```markdown
### 💰 ROI 压测

这个方案现在需要先证明“值得做”，而不仅是“能做”。

问题：这件事的收益准备用哪个指标量化？

为什么重要：如果收益无法量化，就很难和其他需求比较优先级。

我的当前判断：当前方案的成本相对明确，但收益口径还不够清楚。
```

## 7. 后果、灰度与爆炸半径

Use when the proposal may affect production, users, money, or core workflows.

Template:

```markdown
### 🚦 上线风险压测

这个点已经进入发布风险范畴。

问题：如果上线后出现核心链路异常，第一止损动作是什么？

为什么重要：没有止损动作，就无法判断爆炸半径是否可控。

我的当前判断：当前方案需要先明确灰度、回滚或降级策略。
```

## 8. 跨职能视角冲突

Use when the user is thinking from only one role's perspective.

Template:

```markdown
### 🔁 视角切换

我先切到 <PM / Dev / QA / Ops / Data / Manager> 视角看这个问题。

问题：如果我是 <角色>，我最可能质疑这个方案的哪一个点？

为什么重要：跨职能协作中的很多争议，来自不同角色看到的风险不同。

我的当前判断：当前方案主要站在 <当前角色> 视角，还没有充分覆盖 <目标角色> 的担忧。
```
