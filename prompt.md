# AI 提示词收集

热门、流行、高效的 AI 提示词合集，每日更新。

---

# 2026-07-03

## 1. ChatGPT 通用高产提示词

**Prompt：**
```
[你的任务描述]

Before you start, ask me any questions you need so I can give you more context. Be extremely comprehensive.
```
> 来源：Artificial Corner — The Best ChatGPT Prompts for 2026  
> 用法：在任务描述后加上这句，AI 会主动追问细节，减少猜测，输出质量大幅提升。

---

## 2. 结构化的提示词模板

**Prompt：**
```
# 角色
你是一名[专业角色]

# 任务
[具体任务描述]

# 约束
- [约束条件1]
- [约束条件2]

# 输出格式
[指定格式，如 Markdown / JSON / 列表]

# 示例
输入：[示例输入]
输出：[示例输出]
```
> 来源：CSDN — Prompt Engineering 2026 提示词工程指南  
> 用法：用分区（角色/任务/约束/格式/示例）代替一大段话，稳定性和可控性显著提升。

---

## 3. 思维链推理提示词（Chain-of-Thought）

**Prompt：**
```
[复杂推理任务]

Let's think step by step.

First, analyze the problem.
Then, break it down into sub-problems.
For each sub-problem, reason through it carefully.
Finally, synthesize the answer.
```
> 来源：Google Cloud Prompt Engineering Guide  
> 用法：对需要推理的任务（数学、逻辑、分析），先让 AI 输出推理过程再给结论。简单任务慎用，避免浪费 token。

---

## 4. Gemini AI 照片编辑提示词 — 电影级人像

**Prompt：**
```
Recreate the background of this photo to look like [地点/年代/氛围].

Adjust the lighting and clothing to match the exact era and location.
Maintain the subject's facial features and expression.
Enhance the mood with cinematic color grading.
```
> 来源：TechRepublic — 7 Best Gemini Photo Editing Trends in 2026  
> 用法：无需手动调参数，用自然语言描述想要的场景和氛围。

---

## 5. 少样本学习提示词（Few-Shot）

**Prompt：**
```
示例 1：
输入：[示例输入1]
输出：[示例输出1 — 演示所需的风格/语调]

示例 2：
输入：[示例输入2]
输出：[示例输出2]

现在处理这个输入：
[实际输入]
```
> 来源：Google Cloud Prompt Design  
> 用法：给 1-3 个范例，模型模仿范例的能力远强于理解抽象描述。

---

## 6. Agent 任务委派提示词

**Prompt：**
```
You are a project manager AI. Break down the following task into subtasks and delegate each one to the most suitable specialist agent:

Task: [总体任务描述]

For each subtask, provide:
1. Subtask name
2. Assigned specialist role
3. Expected output format
4. Dependencies between subtasks
```
> 来源：Prompt Engineering for AI Engineers (2026)  
> 用法：让 AI 扮演项目经理，自动拆解复杂任务并分派给不同的专业 Agent。

---

## 7. 代码审查与优化提示词

**Prompt：**
```
Review the following code for:
1. Potential bugs and edge cases
2. Performance bottlenecks
3. Code style and readability issues
4. Security vulnerabilities

For each issue found, explain why it's a problem and suggest a fix.

Code:
[粘贴代码]
```
> 来源：IBM 2026 Guide to Prompt Engineering  
> 用法：结构化的代码审查指令，覆盖四个维度，比说"review this code"获得更全面的反馈。

---

## 8. 自适应提示模板

**Prompt：**
```
Based on our conversation history, adapt your response style to match my needs.

Previous context: [对话历史摘要]

Current request: [当前请求]

Respond in a way that:
- Matches the complexity level of my previous questions
- Maintains consistency with information already shared
- Builds on previous conclusions rather than restarting
```
> 来源：Promptitude — The Complete Guide to Prompt Engineering in 2026  
> 用法：让 AI 基于对话历史自适应调整回复风格，适合长对话场景。
