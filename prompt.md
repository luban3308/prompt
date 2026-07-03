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

---

# 2026-07-03 (第二批)

## 9. Claude XML 标签提示法

**Prompt：**
```
<role>You are a [专业角色，如 senior data analyst]</role>

<task>
[具体任务描述，明确输出目标]
</task>

<rules>
- [规则1：输出格式要求]
- [规则2：内容边界]
- [规则3：语气/风格]
</rules>

<context>
[背景信息、数据、文档全文]
</context>
```
> 来源：SurePrompts — 50 Best Claude Prompts in 2026
> 用法：Claude 原生支持 XML 标签结构，用 `<role>` `<task>` `<rules>` `<context>` 包裹分段比纯文本稳定得多。每个标签都是一个明确的上下文边界，Claude 会严格遵循标签内的指令。

---

## 10. RACE 提示框架

**Prompt：**
```
Act as a [ROLE — 角色定义].

[ACTION — 具体要做的事]

Here is the context: [CONTEXT — 背景信息]

Here are examples: [EXAMPLES — 参考范例]

Follow these rules:
- [约束条件]
- [输出格式要求]
```
> 来源：Nigape — AI Prompt Examples 2026
> 用法：RACE = Role + Action + Context + Examples。记不住的模板就用这个四字口诀，涵盖提示词核心要素，适合快速搭建各种场景的 prompt。

---

## 11. 先计划后执行提示词（Plan-First）

**Prompt：**
```
Task: [你的任务]

Before writing any code (or output), do the following:
1. Read through the requirements carefully
2. Identify potential issues, edge cases, or ambiguities
3. Create a step-by-step plan for how you will approach this
4. Present the plan to me for approval

Once I approve the plan, proceed with implementation.
```
> 来源：YouTube — How To Prompt Claude Code Better Than 99% (2026)
> 用法：对复杂编码/写作任务，先让 AI 出方案，批准后再执行。避免 AI 一上来就写错方向，减少返工。Claude Code 的 Plan Mode 核心就是这个思路。

---

## 12. 图片生成结构化提示词（Midjourney / DALL-E）

**Prompt：**
```
[主体描述], [场景/环境], [光线/色调], [构图/角度], [风格参考], [额外参数]

Example:
A photorealistic 3D collector figure of a man in flannel shirt and jeans, displayed on a wooden desk beside a large monitor, dramatic studio lighting, ultra-detailed fabric texture, Sideshow Collectibles quality, --ar 4:5 --v 7
```
> 来源：Medium — Complete List of Prompts & Styles for MidJourney 2026 Edition
> 用法：图片生成提示词的固定配方：主体 → 场景 → 光线 → 构图 → 风格 → 参数。顺序影响权重，越靠前的词权重越高。--ar 控制宽高比，--v 指定模型版本。

---

## 13. 自我反思/自检提示词（Self-Check）

**Prompt：**
```
[你的任务]

After completing the task, review your own output and:
1. Identify any potential errors or omissions
2. Check if all constraints were satisfied
3. Rate confidence in each part of the answer (low/medium/high)
4. Suggest specific improvements if confidence is low
5. Flag any assumptions you made that could affect accuracy
```
> 来源：IBM — 2026 Guide to Prompt Engineering
> 用法：让 AI 对自己的输出进行二次检查，自动纠错。适合事实核查、数据分析、代码生成等对准确性要求高的场景。

---

## 14. Meta-Prompting — 让 AI 帮你写提示词

**Prompt：**
```
You are an expert prompt engineer. I need a prompt for the following task:

Task description: [你想让 AI 做什么]
Target AI model: [ChatGPT / Claude / Gemini]
Desired output format: [格式要求]
Key constraints: [约束条件]

Generate a complete, ready-to-use prompt that I can copy and paste.
The prompt should include role, task, format, constraints, and examples.
Explain why each part is structured this way.
```
> 来源：Artificial Corner / Promptitude — Prompt Engineering Guide 2026
> 用法：不会写 prompt？让 AI 帮你写。描述你的需求，它生成结构化的完整 prompt，还会解释为什么这么写。适合新手快速上手，也适合老手获取灵感。
