#!/usr/bin/env python3
"""Batch append 100+ prompts to prompt.md, avoiding duplicates with existing content."""

import re

FILE = "/Users/tony/develop/openclaw/prompt/prompt.md"

# Read existing content to avoid duplicates
with open(FILE, "r") as f:
    existing = f.read()

# Count existing prompts for proper numbering
existing_count = len(re.findall(r'^## \d+\.', existing, re.MULTILINE))

# First, add today's batch 3 heading
with open(FILE, "a") as f:
    f.write("\n# 2026-07-03 (第三批 批量填充)\n")

# Extract existing prompt headers (titles) to compare
existing_titles = set(re.findall(r'^## \d+\.\s+(.+)', existing, re.MULTILINE))
existing_prompts_lower = set()
# Extract prompt code blocks
for m in re.finditer(r'\*\*Prompt：\*\*\n```\n(.*?)```', existing, re.DOTALL):
    existing_prompts_lower.add(m.group(1).strip().lower()[:80])

def is_duplicate(title, prompt_text):
    if title.strip() in existing_titles:
        return True
    key = prompt_text.strip().lower()[:80]
    if key in existing_prompts_lower:
        return True
    return False

# ============================================
# PROMPTS COLLECTION - organized by category
# ============================================

prompts = []

# ========================
# CATEGORY: Productivity & Work (15 prompts)
# ========================

prompts.append({
    "title": "决策矩阵分析",
    "prompt": """Help me make a decision between these options:
Options: [列举选项]
Priorities (rate 1-10): [列举优先级维度]

Build a weighted decision matrix scoring each option against my priorities (1-10 scale), then give me a clear recommendation with the top 2 reasons why and the top 1 reason I might be wrong.""",
    "source": "AI Academy — 50 Best ChatGPT Prompts 2026",
    "usage": "将模糊的决策转化为结构化比较，附带推荐和被反驳的理由。"
})

prompts.append({
    "title": "会议纪要整理",
    "prompt": """Here are my raw notes from a meeting:
[粘贴原始笔记]

Produce a clean recap with:
(1) one-sentence purpose of the meeting
(2) key decisions made
(3) action items in a table with Owner | Action | Due Date
(4) open questions still to resolve
(5) the next meeting time if mentioned""",
    "source": "AI Academy — 50 Best ChatGPT Prompts 2026",
    "usage": "把零散会议笔记变成结构化纪要。建议会议结束后1小时内使用。"
})

prompts.append({
    "title": "邮件草稿优化",
    "prompt": """Rewrite this email to be more effective:

Current draft: [粘贴邮件]

Recipient: [收件人描述]
Goal: [期望结果]
Tone: [专业/温和/紧急]
Length: [保持简短/适度详细]

Keep the key information but improve clarity, tone, and call-to-action.""",
    "source": "AI Academy / Promptitude 2026",
    "usage": "不重写而是优化，保留原始信息但提升表达效果。"
})

prompts.append({
    "title": "周报自动生成",
    "prompt": """Generate a weekly status report based on these bullet points:

This week's work: [逐条列出完成的工作]
Blockers: [遇到的阻碍]
Next week's plan: [下周计划]

Format as:
- Highlights (top 3 wins)
- Details (organized by project)
- Challenges (with proposed solutions)
- Next week priorities (ranked)""",
    "source": "SurePrompts — Weekly Report Template 2026",
    "usage": "把零散的工作记录变成结构化的周报，节省每周写周报的时间。"
})

prompts.append({
    "title": "OKR 设定助手",
    "prompt": """Help me set OKRs for:

Role: [你的角色/职位]
Timeframe: [季度/半年]
Company goal alignment: [公司目标]
Current status: [当前的进展描述]

Generate:
1. 2-3 Key Results with measurable outcomes
2. Each KR should have: baseline, target, confidence level
3. Suggested initiatives for each KR
4. Potential risks and mitigation""",
    "source": "SurePrompts — 50 Best ChatGPT Prompts 2026",
    "usage": "把模糊的目标转化为可衡量的 OKR。"
})

prompts.append({
    "title": "时间块规划",
    "prompt": """Plan my day using time-blocking:

Tasks: [列出今天所有任务]
Estimated durations: [估计时间]
Meetings: [固定会议]
Energy levels: [精力高峰时段]

Create a schedule that:
- Groups similar tasks together
- Places deep work in peak energy hours
- Includes buffer time between tasks
- Accounts for breaks and meals""",
    "source": "AI Academy Productivity Prompts 2026",
    "usage": "不只是一个待办列表，而是按精力曲线优化排列的日程。"
})

prompts.append({
    "title": "项目复盘（事后分析）",
    "prompt": """Conduct a post-mortem analysis for:

Project: [项目名称]
Timeline: [时间跨度]
Outcome: [成功/失败/部分达成]

Analyze:
1. What went well (and why)
2. What went wrong (root causes, not symptoms)
3. What we learned
4. Action items for next time

Be honest and constructive. Focus on processes, not people.""",
    "source": "IBM 2026 Prompt Engineering Guide",
    "usage": "对已完成项目进行回顾，关注流程而非人，输出可执行的改进项。"
})

prompts.append({
    "title": "优先级排序艾森豪威尔矩阵",
    "prompt": """Help me prioritize these tasks using the Eisenhower Matrix:

Tasks: [列出所有任务]

Sort them into:
1. Urgent & Important — do now
2. Important but Not Urgent — schedule
3. Urgent but Not Important — delegate
4. Neither — eliminate or defer

For each quadrant, explain why it belongs there.""",
    "source": "ClickUp — ChatGPT Prompts for Writing 2026",
    "usage": "用经典四象限法帮你区分哪些该做、哪些该推。"
})

prompts.append({
    "title": "SOP 编写",
    "prompt": """Write a Standard Operating Procedure for:

Process: [流程名称]
Department: [部门]
Audience: [执行者]
Complexity: [简单/中等/复杂]

Structure:
1. Purpose (why this process exists)
2. Prerequisites (what you need before starting)
3. Step-by-step instructions (numbered)
4. Quality checks (how to verify it's done right)
5. Troubleshooting (common issues)
6. Owner and review cadence""",
    "source": "SurePrompts — Business Prompts 2026",
    "usage": "编写标准操作流程，让团队成员可以按步骤执行。"
})

prompts.append({
    "title": "邮件自动化模板",
    "prompt": """Write an email sequence for:

Scenario: [场景说明]
Target audience: [目标受众]
Sequence length: [X封邮件]
Goal: [最终目标]
Tone: [语气]

For each email, provide:
- Subject line (max 60 chars)
- Body (max 150 words)
- Call-to-action
- Follow-up trigger""",
    "source": "SurePrompts — 50 Best Claude Prompts 2026",
    "usage": "生成自动化邮件序列，每封带标题、正文和CTA。"
})

prompts.append({
    "title": "个人 SWOT 分析",
    "prompt": """Help me conduct a personal SWOT analysis:

My role: [职业/角色]
Industry: [行业]
Career goal: [职业目标]
Key skills: [技能列表]
Challenges: [当前面临挑战]

Generate:
Strengths: What advantages do I have?
Weaknesses: What could I improve?
Opportunities: What external chances can I seize?
Threats: What external obstacles do I face?

Follow with 3 strategic recommendations.""",
    "source": "AI Academy Career Prompts 2026",
    "usage": "个人版的 SWOT 分析，附带战略建议。"
})

prompts.append({
    "title": "行动计划拆解",
    "prompt": """Break down this goal into an actionable plan:

Goal: [目标]
Deadline: [截止日期]
Resources available: [可用资源]
Constraints: [限制条件]

Create a plan with:
1. Milestones with dates
2. Weekly action items
3. Dependencies between steps
4. Risk mitigation for each phase
5. Success criteria for each milestone""",
    "source": "Promptitude — Guide to Prompt Engineering 2026",
    "usage": "把大目标拆解成有期限的行动计划，附带风险和备选方案。"
})

prompts.append({
    "title": "陌生邮件沟通",
    "prompt": """Write a cold outreach email:

Recipient: [收件人角色/职位]
Context: [如何知道对方/为什么联系]
Value proposition: [你能提供什么价值]
Desired outcome: [你希望的结果]

The email should:
- Be under 150 words
- Show I've done my research
- Make it easy to say yes
- Include a specific, low-friction ask
- Not sound like a template""",
    "source": "Nigape — AI Prompt Examples 2026",
    "usage": "冷启动邮件模板，突出价值而非需求。"
})

prompts.append({
    "title": "应聘简历定制",
    "prompt": """Tailor my resume for this job:

Job description: [粘贴工作描述]
My current resume: [粘贴简历]

Keep the same facts but:
- Reword bullet points to match keywords from the job description
- Emphasize relevant experience
- Reorder skills by relevance
- Quantify achievements where possible
- Remove less relevant items""",
    "source": "AI Academy — Career & Job Search 2026",
    "usage": "针对特定职位定制简历，匹配关键词但不编造经历。"
})

prompts.append({
    "title": "谈判话术准备",
    "prompt": """Help me prepare for a negotiation:

Context: [谈判背景]
My position: [我方立场]
Their position: [对方可能立场]
Key interests: [双方核心利益]
Walk-away option: [BATNA]

Generate:
1. Opening statement
2. Key talking points
3. Possible objections and responses
4. Concession strategy
5. Closing approach""",
    "source": "Nigape / Techpresso — Business Prompts 2026",
    "usage": "准备谈判话术，包括开场、反驳和让步策略。"
})

# ========================
# CATEGORY: Writing & Content (15 prompts)
# ========================

prompts.append({
    "title": "SEO 博客文章开头",
    "prompt": """Write 5 opening hooks for a blog post about [主题].

Target audience: [目标受众]
Tone: [语气]
Format options:
- Shocking statistic
- Relatable story
- Provocative question
- Controversial statement
- Counter-intuitive fact

Each hook should be 2-3 sentences max.""",
    "source": "AI Prompt Library — 75 Best AI Prompts 2026",
    "usage": "生成5种不同风格的开头，测试哪个转化率最高。"
})

prompts.append({
    "title": "长篇博文完整框架",
    "prompt": """Write a 1,500-word blog post about [主题].

Target audience: [目标受众]
Format:
- Hook intro (2 sentences)
- Problem statement (why this matters)
- 5 subheadings with 2-3 paragraphs each
- Key takeaways (bullet list)
- Conclusion with CTA

SEO keywords to include: [关键词列表]
Tone: [语气]
Include specific examples and data points where possible.""",
    "source": "AI Prompt Library — 75 Best AI Prompts 2026",
    "usage": "完整的长篇博文框架，含 SEO 关键词植入。"
})

prompts.append({
    "title": "产品描述撰写",
    "prompt": """Write a product description for:

Product: [产品名称]
Target audience: [目标用户]
Key features: [核心功能]
Unique value: [差异化卖点]
Tone: [高端/亲民/技术]

Structure:
1. Problem-solution hook (1 sentence)
2. Key benefit (2-3 sentences)
3. Features with user benefits (bullet points)
4. Social proof or specs
5. Call to action""",
    "source": "Nigape — AI Prompt Examples 2026 | Writing & Content",
    "usage": "完整的电商产品描述结构，从痛点到CTA。"
})

prompts.append({
    "title": "新闻稿撰写",
    "prompt": """Write a press release about:

Announcement: [要宣布的事情]
Company: [公司名称]
Date: [发布日期]
Quote from: [发言人姓名及头衔]

Format:
1. Headline (bold, under 20 words)
2. Dateline + lead paragraph (who, what, when, where, why)
3. Body (2-3 paragraphs with key details)
4. Quote paragraph
5. Boilerplate (about the company)
6. Media contact information""",
    "source": "SurePrompts — Writing Templates 2026",
    "usage": "标准新闻稿格式，含引语和公司简介样板。"
})

prompts.append({
    "title": "社交媒体文案矩阵",
    "prompt": """Create social media posts for:

Content to share: [内容描述]
Platforms: [LinkedIn / Twitter/X / Threads / Instagram]
Goal: [品牌曝光/引流/互动]

For each platform, write posts that match:
- Character limits
- Tone conventions
- Hashtag strategy (count and selection)
- Best posting times
- Engagement hooks

Create 3 variations per platform for A/B testing.""",
    "source": "ClickUp — ChatGPT Prompts for Writing 2026",
    "usage": "为同一内容生成跨平台适配的多个版本，支持A/B测试。"
})

prompts.append({
    "title": "改写 & 润色指令",
    "prompt": """Rewrite the following text to be more [清晰/有说服力/专业/简洁]:

Original: [粘贴原文]

Target audience: [目标读者]
Desired tone: [语气]
Length: [保持/缩短/扩展]

Rules:
- Keep all key facts
- Improve readability
- Remove jargon
- Strengthen the main argument
- End with a clear takeaway""",
    "source": "EverythingAI / SurePrompts 2026",
    "usage": "全面润色指令，指定目标读者和语气，保留关键事实。"
})

prompts.append({
    "title": "演讲稿撰写",
    "prompt": """Write a speech about:

Topic: [主题]
Speaker: [演讲者]
Audience: [观众]
Duration: [分钟数]
Occasion: [场合]
Key message: [核心信息]

Structure:
1. Opening (hook + context)
2. Problem or tension
3. Personal story or data point
4. Solution or insight
5. Call to action

Include cues for pacing and emphasis. Write for spoken word, not written text.""",
    "source": "SurePrompts — Creative Prompts 2026",
    "usage": "撰写适合口头表达的演讲稿，含节奏提示。"
})

prompts.append({
    "title": "FAQ 生成",
    "prompt": """Generate an FAQ section for:

Topic/Product: [主题]
Target audience: [受众]
Known questions: [已知问题列表]

For each question, provide:
- Question (as the user would ask it)
- Answer (concise, 2-3 sentences)
- Related links or resources

If there are important questions not in my list, add them.
Organize by category.""",
    "source": "IBM 2026 Prompt Engineering Guide",
    "usage": "从已知问题和产品文档生成结构化的 FAQ。"
})

prompts.append({
    "title": "邮件主题行生成",
    "prompt": """Generate 10 email subject lines for:

Campaign: [活动描述]
Audience: [目标受众]
Goal: [打开/点击/转化]
Tone: [语气]

Each subject line should:
- Be under 60 characters
- Pass the "curiosity gap" test
- Avoid spam trigger words
- Include personalization hook

Rate each one: clickability (1-10) and spam risk (1-10).""",
    "source": "Nigape — AI Prompt Examples 2026",
    "usage": "10个经过垃圾邮件检测的主题行，附带评分。"
})

prompts.append({
    "title": "案例研究框架",
    "prompt": """Write a customer case study:

Company: [客户名称]
Industry: [行业]
Challenge: [客户面临的问题]
Solution: [你提供的方案]
Results: [可量化的成果]

Format:
1. Executive summary (3 sentences)
2. The challenge (detailed context)
3. Our approach (why we chose this solution)
4. Implementation highlights
5. Measurable results (with specific numbers)
6. Customer quote
7. Key takeaways""",
    "source": "ClickUp — LinkedIn Case Study Prompt 2026",
    "usage": "客户案例标准框架，数据和引语驱动。"
})

prompts.append({
    "title": "博客文章改写为 LinkedIn 帖",
    "prompt": """Rewrite this blog post as a LinkedIn post:

Blog post: [粘贴博客内容]
Target: LinkedIn professionals in [行业]
Goal: [品牌曝光/引发讨论/吸引关注]

Convert to:
- Hook (1 sentence)
- Key insight (2-3 sentences)
- Supporting point or story
- Call to action or question
- 3-5 relevant hashtags

Keep it under 1,200 characters. Write conversationally.""",
    "source": "ClickUp — ChatGPT Prompts for Writing 2026",
    "usage": "将博客文章转化为 LinkedIn 风格的发帖，保留核心观点。"
})

prompts.append({
    "title": "创意写作：故事情节生成",
    "prompt": """Generate a story premise based on:

Genre: [科幻/奇幻/悬疑/爱情]
Key elements: [核心元素]
Tone: [轻松/黑暗/幽默]

Provide:
1. Logline (1 sentence)
2. Main character description
3. World-building details
4. Three-act structure outline
5. Thematic question the story explores
6. Potential plot twists""",
    "source": "SurePrompts — Creative Prompts 41-45 2026",
    "usage": "完整的故事创意生成，从一句话梗概到三幕结构。"
})

prompts.append({
    "title": "角色设定开发",
    "prompt": """Develop a character for my story:

Role: [主角/反派/配角]
Archetype: [经典原型]
Setting: [故事世界观]

Create:
1. Name and basic stats (age, occupation, background)
2. External traits (appearance, mannerisms, speech patterns)
3. Internal traits (motivations, fears, flaws, desires)
4. Backstory (formative event that shaped them)
5. Arc (how they change throughout the story)
6. Relationships (key connections to other characters)""",
    "source": "SurePrompts — Creative Writing 2026",
    "usage": "从外表到内心到成长弧线的完整角色设定。"
})

prompts.append({
    "title": "技术文档编写",
    "prompt": """Write technical documentation for:

Feature/API: [功能或API名称]
Target audience: [开发者/最终用户/运维]
Experience level: [初级/中级/高级]

Include:
1. Overview (what it does, why it exists)
2. Prerequisites
3. Installation/setup steps
4. Usage examples with code
5. Configuration options
6. Error codes and troubleshooting
7. Best practices

Format code examples for copy-paste. Include expected outputs.""",
    "source": "SurePrompts — Technical Documentation 2026",
    "usage": "技术文档完整模板，含代码示例和排错指南。"
})

# ========================
# CATEGORY: Learning & Research (10 prompts)
# ========================

prompts.append({
    "title": "复杂概念速通（费曼学习法）",
    "prompt": """Explain [概念] to me using the Feynman Technique.

First, explain it as if I'm a bright 12-year-old (simple analogies, no jargon).
Then, explain it at an undergraduate level (key theories, models).
Finally, at a graduate level (current debates,open questions).

For each level, identify the most common misconceptions.""",
    "source": "AI Academy — Learning & Self-Improvement 2026",
    "usage": "三层递进解释法，从简单到专业，附带常见误解。"
})

prompts.append({
    "title": "论文/论文文献总结",
    "prompt": """Summarize this research paper/article:

Title: [标题]
Full text: [粘贴全文]

Provide:
1. Research question (1 sentence)
2. Methodology overview
3. Key findings (3-5 bullet points)
4. Limitations
5. Implications (what this means for the field)
6. Related papers I should read next

Use language accessible to someone with basic domain knowledge.""",
    "source": "IBM / SurePrompts — Research Summary 2026",
    "usage": "论文总结模板，适合快速理解新领域的研究。"
})

prompts.append({
    "title": "个性化学习计划",
    "prompt": """Create a personalized learning plan for:

Topic: [学习主题]
Current level: [零基础/初级/中级]
Time available: [每周X小时]
Learning style: [阅读/视频/实践]
Goal: [具体目标]
Deadline: [截止日期]

Design a curriculum with:
1. Prerequisite knowledge checklist
2. Weekly topics (ordered, building on each other)
3. Resources for each week (free/paid)
4. Practice exercises
5. Milestone projects
6. Success metrics""",
    "source": "AI Academy — Learning Prompts 2026",
    "usage": "根据你的水平、时间和学习风格定制的学习路线图。"
})

prompts.append({
    "title": "Socratic 问答学习",
    "prompt": """Teach me about [主题] using the Socratic method.

Do not give me answers directly. Instead:
1. Ask me a series of questions that lead to understanding
2. Based on my answers, probe deeper
3. Point out contradictions in my thinking
4. Guide me toward the correct understanding
5. Only explain after I've attempted to reason through

Start with the most fundamental question about this topic.""",
    "source": "AI Academy / Prompt Engineering Guide 2026",
    "usage": "苏格拉底式教学法：通过提问引导你自己发现答案。"
})

prompts.append({
    "title": "知识卡片（Anki/闪卡）生成",
    "prompt": """Convert this content into study flashcards:

Topic: [主题]
Content: [粘贴要学习的内容]

Create flashcards following these rules:
1. One fact per card
2. Front: clear question or prompt
3. Back: concise answer (max 3 sentences)
4. Include mnemonics where helpful
5. Tag each card by category

Format as: Q: [问题] | A: [答案] | Tag: [标签]""",
    "source": "AI Academy — Learning Prompts 2026",
    "usage": "把学习材料转为闪卡格式，适合导入 Anki 等记忆软件。"
})

prompts.append({
    "title": "对比分析（概念 A vs 概念 B）",
    "prompt": """Compare and contrast [概念A] vs [概念B]:

For each, analyze:
1. Core definition
2. Key principles
3. Real-world applications
4. Strengths
5. Weaknesses/limitations
6. When to use each

Then provide:
- A decision tree to help choose between them
- A scenario where you'd use both together
- Common misconceptions about each""",
    "source": "Promptitude — Best Practices 2026",
    "usage": "两个概念的全面对比，含决策树辅助选择。"
})

prompts.append({
    "title": "行业研究速览",
    "prompt": """Give me a fast overview of the [行业] industry:

Focus areas:
1. Market size and growth rate
2. Key players and market share
3. Latest trends (last 12 months)
4. Regulatory landscape
5. Technology shifts
6. Entry barriers

For each, include specific data points or examples.
Format as a briefing memo for someone new to the industry.""",
    "source": "IBM 2026 Prompt Engineering Guide",
    "usage": "行业速览简报格式，涵盖市场、玩家、趋势和监管。"
})

prompts.append({
    "title": "英文语法纠错 & 改进",
    "prompt": """Proofread and improve this English text:

Text: [粘贴英文文本]

For each correction, explain:
1. What was wrong (rule explanation)
2. The correction
3. Why the correction is better

Categorize issues as:
- Grammar errors
- Word choice / vocabulary
- Sentence structure
- Tone and style
- Clarity issues

Provide a clean corrected version at the end.""",
    "source": "Nigape / SurePrompts 2026",
    "usage": "英文校对+改进，每条修正带规则解释。"
})

prompts.append({
    "title": "多语言翻译 + 本地化",
    "prompt": """Translate and localize the following text:

Text: [粘贴原文]
Source language: [源语言]
Target language: [目标语言]
Target locale: [国家/地区]
Audience: [目标受众]
Tone: [语气]

Requirements:
- Natural, not literal translation
- Adapt idioms and cultural references
- Keep technical terms consistent
- Preserve formatting
- Note any text that might be culturally sensitive
- Provide alternative translations for ambiguous phrases""",
    "source": "Google Cloud — Prompt Engineering Guide 2026",
    "usage": "专业级翻译+本地化，处理习语和文化差异。"
})

# ========================
# CATEGORY: Coding & Development (15 prompts)
# ========================

prompts.append({
    "title": "自动化脚本需求描述 → 代码",
    "prompt": """Generate a script that automates this task:

Task description: [描述你要自动化的任务]
Input: [输入格式]
Output: [期望输出]
Language: [Python/Bash/Node.js]
Constraints: [限制条件]

The script should:
- Include error handling
- Accept command-line arguments or config
- Log progress
- Handle edge cases
- Include a --help flag""",
    "source": "EverythingAI — Coding Prompts 2026",
    "usage": "从自然语言需求直接生成自动化脚本，含错误处理和帮助信息。"
})

prompts.append({
    "title": "SQL 查询优化",
    "prompt": """Optimize this slow SQL query:

Query: [粘贴SQL]
Database: [PostgreSQL/MySQL/MongoDB]
Current execution time: [时间]
Table sizes: [行数估计]
Current indexes: [现有索引]

Suggest:
1. Query optimization (rewrite the query)
2. Index recommendations
3. Schema improvements
4. Caching strategies
5. Alternative approaches

Explain why each change improves performance.""",
    "source": "EverythingAI — Coding Prompts 2026",
    "usage": "SQL性能优化，从查询重写、索引到缓存策略。"
})

prompts.append({
    "title": "API 端点设计",
    "prompt": """Design a REST API endpoint for:

Resource: [资源名称]
Operations needed: [CRUD/特定操作]
Framework: [Express/FastAPI/Spring Boot]
Auth: [认证方式]

Provide:
1. Route definitions with HTTP methods
2. Request/response schemas (JSON)
3. Validation rules
4. Error response format
5. Rate limiting approach
6. Pagination (if listing)
7. Example curl commands""",
    "source": "EverythingAI — API Endpoint Generator 2026",
    "usage": "完整 API 端点设计，从路由到验证到示例。"
})

prompts.append({
    "title": "React 组件生成",
    "prompt": """Generate a React component for:

Purpose: [组件功能描述]
Props: [属性列表含类型]
State management: [useState/useContext/Redux]
Styling: [Tailwind/CSS Modules/Styled Components]

Include:
- TypeScript types
- Error boundaries
- Loading states
- Empty states
- Accessibility attributes
- Unit test structure""",
    "source": "EverythingAI — React Component Generator 2026",
    "usage": "生产级 React 组件，含错误边界、加载、空状态和无障碍。"
})

prompts.append({
    "title": "数据库 Schema 设计",
    "prompt": """Design a database schema for:

Application: [应用描述]
Database type: [SQL/NoSQL]
Key entities: [主要实体列表]

Generate:
1. Entity definitions with all fields
2. Relationships (foreign keys, references)
3. Indexes for performance
4. Sample migration script
5. Common query patterns
6. Normalization notes""",
    "source": "EverythingAI — Database Schema Designer 2026",
    "usage": "从应用描述到完整的数据库设计。"
})

prompts.append({
    "title": "堆栈跟踪分析 & 排错",
    "prompt": """Analyze this stack trace and help me fix it:

[粘贴完整堆栈跟踪]

Context:
- When it happens: [场景]
- Recent changes: [近期改动]
- Environment: [开发/预发/生产]

Provide:
1. Line-by-line stack trace explanation (plain English)
2. Root cause identification
3. Fix implementation (code)
4. How to prevent in the future""",
    "source": "EverythingAI — Debugging & Troubleshooting 2026",
    "usage": "逐行分析堆栈跟踪，用普通人能懂的语言解释。"
})

prompts.append({
    "title": "内存泄漏检测",
    "prompt": """Identify potential memory leaks in:

[粘贴代码]

Language: [JavaScript/Python/Java/Go]
Symptoms: [描述内存问题]
Environment: [运行环境]

Analyze:
- Potential leak sources
- Object retention issues
- Event listener problems
- Closure-related leaks
- Recommended profiling approach
- Fix for each issue found""",
    "source": "EverythingAI — Memory Leak Detection 2026",
    "usage": "代码内存泄漏扫描，从闭环到事件监听到引用保留。"
})

prompts.append({
    "title": "正则表达式生成",
    "prompt": """Create a regex pattern to:

Task: [描述要匹配的内容]

Valid examples:
- [示例1]
- [示例2]

Invalid examples:
- [示例1]
- [示例2]

Provide:
1. The regex pattern
2. Explanation of each part
3. Test cases showing matches and non-matches
4. Language-specific implementation (escaping, flags)
5. Common edge cases and gotchas""",
    "source": "EverythingAI — Regex Pattern Generator 2026",
    "usage": "正则表达式生成+逐段解释+测试用例。"
})

prompts.append({
    "title": "单元测试套件生成",
    "prompt": """Generate comprehensive unit tests for:

[粘贴要测试的函数/类]

Testing framework: [Jest/pytest/JUnit]
Coverage goal: [关键路径/边缘情况/错误处理]

Cover:
1. Happy path (normal inputs)
2. Edge cases (boundary values)
3. Error cases (invalid inputs)
4. State-based tests (if applicable)
5. Mock external dependencies

Include test descriptions that document intent.""",
    "source": "EverythingAI — Unit Test Suite Generator 2026",
    "usage": "完整单元测试套件，覆盖正向/边界/错误三种场景。"
})

prompts.append({
    "title": "代码重构：可读性改进",
    "prompt": """Refactor this code to improve readability and maintainability:

[粘贴代码]

Goals:
- Reduce complexity (cyclomatic complexity)
- Improve naming (variables, functions, classes)
- Extract reusable functions
- Follow SOLID principles
- Add type hints/annotations
- Add comments where logic is non-obvious

Provide before/after comparison with explanations for each change.""",
    "source": "EverythingAI — Code Refactoring 2026",
    "usage": "代码重构的完整流程，前后对比并逐条解释。"
})

prompts.append({
    "title": "设计模式推荐",
    "prompt": """Recommend appropriate design patterns for:

Problem: [描述编码挑战]
Language: [编程语言]
Current approach: [现有代码或描述]

Suggest:
1. Best design pattern to use
2. Why it fits this problem
3. Example implementation
4. Pros and cons of this approach
5. Alternative patterns and when they'd be better""",
    "source": "EverythingAI — Design Pattern Recommendation 2026",
    "usage": "根据编码挑战推荐最适合的设计模式。"
})

prompts.append({
    "title": "Dockerfile + docker-compose 生成",
    "prompt": """Generate Docker configuration for:

Project type: [语言/框架]
Runtime: [Node.js/Python/Go/Java]
Port: [端口号]
Dependencies: [依赖说明]
Environment variables: [环境变量列表]

Provide:
1. Dockerfile (multi-stage if applicable)
2. .dockerignore
3. docker-compose.yml (including any services like DB, Redis)
4. Health check configuration
5. Resource limits
6. Security best practices (non-root user, etc.)""",
    "source": "EverythingAI / SurePrompts — DevOps Prompts 2026",
    "usage": "生产级 Docker 配置生成，含多阶段构建和安全最佳实践。"
})

prompts.append({
    "title": "Changelog / Release Notes 生成",
    "prompt": """Generate release notes for version [版本号]:

Git commits since last release:
[粘贴 git log 输出]

Format:
1. Summary section (one-paragraph overview)
2. New features (with user-facing descriptions)
3. Bug fixes (with issue references)
4. Performance improvements
5. Breaking changes (bold + migration notes)
6. Deprecations
7. Credits to contributors

Categorize commits appropriately. Use plain English.""",
    "source": "SurePrompts — Dev Tools 2026",
    "usage": "从 git log 自动生成结构化的发布说明。"
})

prompts.append({
    "title": "Git 操作指南",
    "prompt": """Help me with this Git scenario:

Situation: [描述你的Git困境]
Current branch: [当前分支]
Goal: [你想达到的状态]

Provide:
1. Step-by-step commands to execute
2. What each command does (explain in plain English)
3. What could go wrong and how to recover
4. Dry-run equivalent if available
5. Best practice for next time""",
    "source": "SurePrompts / EverythingAI 2026",
    "usage": "Git操作指导，告诉你怎么做、为什么这么做、做错了怎么恢复。"
})

# ========================
# CATEGORY: Marketing & Growth (10 prompts)
# ========================

prompts.append({
    "title": "营销策略框架",
    "prompt": """Create a marketing strategy for:

Product/Service: [产品描述]
Target market: [目标市场]
Budget: [预算范围]
Timeline: [时间周期]
Current traction: [现有用户/收入]

Framework:
1. Market analysis (TAM, SAM, SOM)
2. Target personas (3 segments max)
3. Positioning statement
4. Channel strategy (which channels and why)
5. Content pillars (4-5 themes)
6. Launch tactics (first 90 days)
7. Success metrics with targets""",
    "source": "AiledGrowth — ChatGPT Prompts for Marketing 2026",
    "usage": "完整营销策略框架，从市场分析到执行计划。"
})

prompts.append({
    "title": "Landing Page 文案",
    "prompt": """Write landing page copy for:

Product: [产品名称]
Unique value prop: [独特价值主张]
Target audience: [目标用户]
Key features: [核心功能]
Social proof: [可用的用户评价/数据]

Sections to write:
1. Above the fold (hero headline + subheadline + CTA)
2. Problem section (pain points)
3. Solution section (how we solve it)
4. Features section (benefits, not just features)
5. Testimonials / social proof
6. FAQ (top 5 questions)
7. Final CTA

Tone: [语气]. Include A/B test variants for the hero headline.""",
    "source": "AiledGrowth / Promptitude 2026",
    "usage": "完整落地页文案，含A/B测试用的标题变体。"
})

prompts.append({
    "title": "A/B 测试假设生成",
    "prompt": """Generate A/B test hypotheses for:

Page/Feature: [页面或功能]
Current metric: [当前指标]
Goal: [提升的指标]

Generate 5 test hypotheses, each including:
1. Hypothesis statement (if we change X, then Y will happen)
2. Proposed change (specific)
3. Expected impact (estimated improvement with rationale)
4. Risk level (low/medium/high)
5. Sample size needed
6. Test duration estimate
7. Success metric""",
    "source": "AiledGrowth — Growth Experimentation 2026",
    "usage": "数据驱动的A/B测试假设生成，附带样本量和时长估计。"
})

prompts.append({
    "title": "SEO 关键词策略",
    "prompt": """Develop an SEO keyword strategy for:

Website: [网站描述]
Niche: [细分领域]
Current authority: [网站权重/域名年龄]

Provide:
1. Head keywords (high volume, competitive)
2. Long-tail keywords (lower volume, targeted)
3. Question-based keywords (for featured snippets)
4. Keyword clusters (group by topic)
5. Content gap analysis (what competitors rank for that you don't)
6. Suggested content pieces for each cluster
7. Internal linking strategy""",
    "source": "Nigape / ClickUp — SEO Prompts 2026",
    "usage": "SEO 关键词全策略，从头部词到长尾词到内容缺口。"
})

prompts.append({
    "title": "广告文案生成（Google/FB）",
    "prompt": """Write ad copy for:

Platform: [Google Ads / Facebook Ads / LinkedIn Ads]
Product: [产品]
Audience: [定向受众]
Goal: [点击/转化/品牌曝光]

Generate:
- 5 headlines (max 30 chars for Google)
- 3 descriptions (max 90 chars)
- 2 calls-to-action

For each, include:
- Emotional trigger
- Value proposition
- Urgency element (if applicable)
- Predicted CTR ranking

Note which emotional triggers each variant uses.""",
    "source": "AiledGrowth — Marketing Prompts 2026",
    "usage": "广告文案多版本生成，含情感触发因素分析。"
})

prompts.append({
    "title": "内容日历规划",
    "prompt": """Plan a content calendar for:

Channel: [博客/Newsletter/社交媒体]
Topic cluster: [主题领域]
Frequency: [周更/日更]
Duration: [一个月/季度]

Generate:
1. Theme for each week/month
2. Content pieces with titles
3. Content format (article/video/infographic)
4. Distribution plan (which channels)
5. Key dates/hooks to leverage
6. Cross-promotion opportunities
7. Repurposing strategy (one piece → multiple formats)""",
    "source": "ClickUp / AiledGrowth 2026",
    "usage": "内容日历规划，含重新利用策略（一鱼多吃）。"
})

prompts.append({
    "title": "销售跟进邮件序列",
    "prompt": """Write a sales follow-up sequence for:

Lead type: [潜客类型]
Initial contact: [首次接触方式]
Product: [产品/服务]
Buyer persona: [决策者画像]

Email sequence (5 emails):
1. Day 1 — Value-add follow-up (not just checking in)
2. Day 3 — Case study or social proof
3. Day 7 — Specific use case relevant to them
4. Day 14 — Offer a demo or trial
5. Day 21 — Breakup email (polite, with one last reason)

Each email: subject line (max 50 chars), body (max 100 words), single CTA.""",
    "source": "AiledGrowth — Sales Prompts 2026",
    "usage": "完整的销售跟进序列，从触达到分手邮件。"
})

prompts.append({
    "title": "品牌定位声明",
    "prompt": """Develop a brand positioning statement for:

Company: [公司名称]
Product: [产品/服务]
Target customers: [目标客户]
Competitors: [主要竞争对手]
Differentiation: [现有差异化]

Generate:
1. Positioning statement (fill-in-the-blank format)
2. Brand personality (5 traits)
3. Voice and tone guidelines
4. Key messages (3 pillars)
5. Proof points (evidence for each claim)
6. Positioning pitfalls to avoid""",
    "source": "AiledGrowth — Strategy Prompts 2026",
    "usage": "品牌定位完整方案，从声明到语调和证明点。"
})

prompts.append({
    "title": "解锁邮件营销",
    "prompt": """Write a re-engagement email for:

Subscriber segment: [不活跃时间段]
Original opt-in reason: [订阅原因]
Value they got before: [之前的价值]

The email should:
1. Acknowledge the silence (not ignore it)
2. Provide a compelling reason to re-engage
3. Make it easy to say "still interested" (single click)
4. Include an unsubscribe option prominently
5. Offer an incentive if appropriate

Subject line options (3 variants).""",
    "source": "Nigape — AI Prompt Examples 2026",
    "usage": "重新激活沉寂用户的邮件，承认沉默并给予重新参与的理由。"
})

prompts.append({
    "title": "用户反馈 → 产品需求文档",
    "prompt": """Convert these user feedback items into a product requirements document:

User feedback: [粘贴用户反馈]

Structure:
1. Problem statement (from user perspective)
2. User stories (as a [user], I want [goal], so that [reason])
3. Success metrics (how we measure this solves the problem)
4. Proposed solution (high-level)
5. Scope: in-scope vs out-of-scope
6. Technical considerations
7. UX requirements
8. Priority ranking (P0/P1/P2)""",
    "source": "SurePrompts — Feature Specification 2026",
    "usage": "把零散的用户反馈转化为可执行的 PRD。"
})

# ========================
# CATEGORY: Business & Analysis (10 prompts)
# ========================

prompts.append({
    "title": "商业模式画布生成",
    "prompt": """Generate a Business Model Canvas for:

Business idea: [描述]
Industry: [行业]
Target customer: [目标客户]

Fill in all 9 building blocks:
1. Customer Segments
2. Value Propositions
3. Channels
4. Customer Relationships
5. Revenue Streams
6. Key Resources
7. Key Activities
8. Key Partnerships
9. Cost Structure

For each block, provide specific details and assumptions.
Flag any block that needs more research.""",
    "source": "AiledGrowth / SurePrompts — Business 2026",
    "usage": "从商业想法生成完整的九宫格商业模式画布。"
})

prompts.append({
    "title": "竞品分析矩阵",
    "prompt": """Perform a competitive analysis for:

Our product: [产品]
Competitors: [竞品列表]
Market: [市场/行业]

For each competitor, analyze:
1. Product features (feature comparison matrix)
2. Pricing model
3. Target audience
4. Strengths (what they do better)
5. Weaknesses (gaps we can exploit)
6. Market positioning
7. Recent moves (product launches, acquisitions)

Summary: our competitive advantage and recommended strategy.""",
    "source": "SurePrompts — Competitive Analysis 2026",
    "usage": "完整竞品分析，含特征对比矩阵和竞争策略建议。"
})

prompts.append({
    "title": "定价策略分析",
    "prompt": """Help me develop a pricing strategy for:

Product: [产品描述]
Cost: [成本结构]
Competitors pricing: [竞品定价]
Target market: [目标市场]
Value metric: [按什么收费]

Analyze:
1. Pricing models to consider (subscription/one-time/freemium/tiered)
2. Recommended price points with rationale
3. Psychology of each price point
4. Discount/bundle strategy
5. Enterprise pricing approach
6. Price sensitivity factors
7. Testing methodology for pricing""",
    "source": "SurePrompts — Business Prompts 2026",
    "usage": "定价策略分析，含心理定价和折扣策略。"
})

prompts.append({
    "title": "风险登记表",
    "prompt": """Create a risk register for:

Project: [项目名称]
Scope: [项目范围]
Stakeholders: [关键干系人]

Identify and assess risks:

Risk | Probability (1-5) | Impact (1-5) | Risk Score | Mitigation Strategy | Contingency Plan | Owner

For each risk:
- Describe the risk clearly
- Rate probability and impact
- Calculate risk score (P × I)
- Primary mitigation
- Backup plan if mitigation fails
- Assign owner""",
    "source": "IBM 2026 Guide to Prompt Engineering",
    "usage": "生成完整风险登记表，含概率、影响评分和应对策略。"
})

prompts.append({
    "title": "会议议程生成",
    "prompt": """Create a meeting agenda for:

Meeting type: [周会/项目评审/1:1/头脑风暴]
Duration: [X分钟]
Participants: [参与者角色]
Key topics: [需要讨论的事项]

Structure:
1. Pre-reading (what to review before the meeting)
2. Agenda items with time boxes
3. For each item: owner, format (discuss/decide/inform), desired outcome
4. Decision log template
5. Action items section

Total: keep under 60% of meeting time allocated to leave room for discussion.""",
    "source": "AI Academy — Productivity Prompts 2026",
    "usage": "高效会议议程，每项标注决策类型和期望成果。"
})

prompts.append({
    "title": "数据解读报告",
    "prompt": """Interpret this data and provide actionable insights:

Data: [粘贴数据表格或描述]
Context: [数据背景]
Question: [想通过数据回答的问题]

Provide:
1. Key findings (top 3-5)
2. Trends and patterns
3. Statistical significance (where applicable)
4. Data quality caveats
5. Actionable recommendations
6. What additional data would help

Avoid: over-interpreting noise, suggesting causality from correlation.""",
    "source": "SurePrompts — Data Interpretation 2026",
    "usage": "数据解读模板，含统计显著性和数据质量警告。"
})

prompts.append({
    "title": "投资人更新邮件",
    "prompt": """Write an investor update email:

Company name: [公司名]
Period: [报告周期]
Key metrics: [关键数据]
Milestones achieved: [里程碑]
Challenges: [面临的挑战]
Next quarter goals: [下季度目标]
Ask (if any): [需要什么帮助]

Structure:
1. Quick summary (3 bullet points)
2. Key metrics table (current vs previous vs target)
3. Narrative (what happened and why)
4. Challenges and how we're addressing them
5. Ask / how they can help
6. Forward-looking outlook""",
    "source": "SurePrompts — Investor Update 2026",
    "usage": "投资人更新邮件模板，快速总结+数据表格+叙事。"
})

prompts.append({
    "title": "项目章程",
    "prompt": """Write a project charter for:

Project name: [项目名]
Problem statement: [要解决的问题]
Proposed solution: [解决方案]
Stakeholders: [干系人]
Budget: [预算范围]
Timeline: [时间线]

Include:
1. Project purpose and justification
2. Objectives and success criteria (SMART)
3. High-level scope (what's in, what's out)
4. Key deliverables
5. Milestone schedule
6. Budget estimate
7. Risk and assumptions
8. Team structure and roles
9. Approval requirements""",
    "source": "IBM / SurePrompts 2026",
    "usage": "项目章程完整模板，用于项目立项和干系人对齐。"
})

prompts.append({
    "title": "财务模型基础",
    "prompt": """Build a simple financial model for:

Business type: [业务类型]
Revenue model: [收入模式]
Cost structure: [成本结构]
Growth assumptions: [增长假设]
Time horizon: [X年]

Generate:
1. Revenue projection (monthly, by revenue stream)
2. Cost breakdown (fixed, variable, COGS)
3. Gross margin analysis
4. Operating expenses
5. Cash flow projection
6. Unit economics (CAC, LTV, payback period)
7. Key metrics dashboard
8. Breakeven analysis

Flag key assumptions and their sensitivity.""",
    "source": "SurePrompts — Financial Analysis 2026",
    "usage": "基础的财务模型搭建，含单位经济模型和盈亏平衡分析。"
})

# ========================
# CATEGORY: Specialized AI Agent Prompts (8 prompts)
# ========================

prompts.append({
    "title": "AI Agent 系统提示词编写",
    "prompt": """Write a system prompt for an AI agent that:

Role: [Agent的角色]
Primary task: [核心任务]
Tools available: [可调用工具]
Constraints: [行为约束]
Output format: [输出格式要求]
Personality: [个性特征]

The system prompt should:
1. Define agent identity clearly
2. List available tools with when to use each
3. Set behavioral guardrails
4. Define output structure
5. Handle edge cases (ambiguous requests, errors)
6. Include examples of good interactions

Use clear XML or markdown structure.""",
    "source": "GitHub — ai-boost/awesome-prompts 2026",
    "usage": "为 AI Agent 编写系统提示词，定义身份、工具、边界和输出格式。"
})

prompts.append({
    "title": "Multi-Agent 任务编排",
    "prompt": """Orchestrate a multi-agent system for:

Task: [总体任务]
Specialists needed: [需要的专业Agent角色]
Coordination needs: [协调要求]

Define:
1. Agent roles and responsibilities
2. Communication protocol between agents
3. Task decomposition and assignment
4. Handoff criteria between agents
5. Quality control checkpoints
6. Escalation path for failures
7. Output aggregation format

Use a team pipeline: plan → spec → exec → verify → fix.""",
    "source": "GitHub — ai-boost awesome-prompts (Oh My ClaudeCode) 2026",
    "usage": "多 Agent 系统编排，从规划到验证的完整流水线。"
})

prompts.append({
    "title": "自改进 Agent 设计",
    "prompt": """Design a self-improving agent that:

Task domain: [任务领域]
Success metric: [衡量标准]
Feedback source: [反馈来源]

The agent should:
1. Log every interaction and outcome
2. Extract lessons from failures
3. Update its own prompt/skills based on lessons
4. Build cross-session memory
5. Track confidence in its knowledge
6. Know when to ask for help
7. Measure improvement over time

Include the reflection loop: act → observe → reflect → adjust.""",
    "source": "GitHub — ai-boost/awesome-prompts (Hermes Agent) 2026",
    "usage": "自改进 Agent 设计，含反思循环和跨 session 记忆。"
})

prompts.append({
    "title": "MCP 工具定义提示词",
    "prompt": """Define a MCP (Model Context Protocol) tool for an AI agent:

Tool name: [工具名]
Description: [工具功能描述]
Input schema: [输入参数格式]
Output format: [输出格式]
Error handling: [错误处理方式]
Rate limits: [频率限制]

For each parameter, define:
- Name
- Type (string/number/boolean/object)
- Required or optional
- Description
- Examples
- Validation rules

Include usage examples showing when this tool should be invoked.""",
    "source": "GitHub — f/prompts.chat 2026 / MCP Protocol Docs",
    "usage": "为 AI Agent 定义 MCP 工具接口，含参数验证和使用示例。"
})

prompts.append({
    "title": "Prompt 注入防御提示词",
    "prompt": """Add security guardrails to this system prompt:

System prompt: [粘贴现有system prompt]

Add protection against:
1. Prompt injection (ignore instructions from user content)
2. Role-playing attempts (do not pretend to be someone else)
3. Output manipulation attempts
4. Data exfiltration attempts
5. Jailbreaking attempts

The guardrails should:
- Be explicit rules, not suggestions
- Not harm legitimate functionality
- Include output filtering rules
- Define what to do when an attack is detected
- Be written in a way that's hard to override""",
    "source": "IBM / OWASP LLM Top 10 / Prompt Security 2026",
    "usage": "给系统提示词加上安全护栏，防御提示注入和越狱攻击。"
})

prompts.append({
    "title": "温度与参数调优指令",
    "prompt": """Optimize generation parameters for:

Task type: [创意写作/代码生成/事实问答/翻译]
Model: [使用的模型]
Desired output characteristics: [期望的输出特征]

Recommend:
1. Temperature (0.0-2.0) — creativity vs determinism
2. Top-p (nucleus sampling)
3. Top-k sampling
4. Frequency penalty (diversity)
5. Presence penalty (topic variety)
6. Max tokens
7. Stop sequences

Explain the tradeoffs for each parameter.
Provide recommended ranges for A/B testing.""",
    "source": "Google Cloud / IBM Prompt Engineering Guide 2026",
    "usage": "针对不同任务类型推荐最优的生成参数组合。"
})

prompts.append({
    "title": "RAG 系统查询优化",
    "prompt": """Optimize this RAG (Retrieval-Augmented Generation) query:

Knowledge base: [知识库描述]
Query: [原始查询]
Chunking strategy: [分段方式]
Embedding model: [嵌入模型]
Top-k: [检索数量]

Improve by:
1. Query rewriting (expand/compress the query)
2. HyDE (generate hypothetical document first)
3. Multi-query retrieval (multiple query variations)
4. Reranking strategy
5. Context window optimization
6. Citation format

Explain why each change improves retrieval quality.""",
    "source": "Prompt Engineering Guide — RAG Best Practices 2026",
    "usage": "RAG 系统查询优化，含查询改写、HyDE 和重排序。"
})

# ========================
# CATEGORY: Creative & Image Generation (8 prompts)
# ========================

prompts.append({
    "title": "DALL-E / GPT Image 照片级产品图",
    "prompt": """Generate a photorealistic product image for:

Product: [产品描述]
Setting: [场景]
Lighting: [Natural/Studio/Dramatic]
Angle: [拍摄角度]
Style: [风格参考]

The image should:
- Look like a professional commercial photograph
- Have realistic lighting and shadows
- Show the product clearly
- Include context-appropriate props
- Have a clean, usable background

Specify aspect ratio and quality parameters.""",
    "source": "AI Prompt Library — AI Image Prompts 2026",
    "usage": "产品摄影级图片生成提示词，含布景、光线和角度。"
})

prompts.append({
    "title": "Midjourney 风格化艺术肖像",
    "prompt": """Create an artistic portrait with these specifications:

Subject: [人物描述]
Art style: [油画/水彩/赛博朋克/水墨/3D渲染]
Lighting: [伦勃朗光/蝴蝶光/侧光]
Color palette: [色调]
Vibe: [氛围]
--ar [宽高比] --v [版本] --s [风格化程度]

Parameters to adjust:
- --stylize (s): how artistic vs literal
- --chaos (c): variation in composition
- --weird (w): experimental output
- --iw: image weight (if using reference image)""",
    "source": "Medium — Complete MidJourney Prompt List 2026",
    "usage": "Midjourney 艺术肖像生成，含风格化参数调优。"
})

prompts.append({
    "title": "3D 收藏手办提示词",
    "prompt": """Generate a 3D collector figure render:

Character: [角色描述]
Style: [收藏级手办品质]
Pose: [姿势]
Accessories: [道具]
Display: [展示方式]

Use descriptors like:
Hyper-detailed 1:6 scale collector figure
Sideshow Collectibles quality
Professional studio lighting
Ultra-realistic skin and fabric texture
Displayed with retail packaging box
--ar 4:5""",
    "source": "Medium — MidJourney 2026 Trending Styles",
    "usage": "2026年非常火的 3D 收藏手办风格提示词。"
})

prompts.append({
    "title": "UI/UX 界面截图生成",
    "prompt": """Generate a UI mockup screenshot for:

App type: [移动端/Web端]
Screen: [页面名称]
Design style: [设计系统/风格]
Brand colors: [品牌色]
Content: [占位内容类型]

The output should:
- Look like a real app screenshot
- Follow platform design guidelines (iOS/Android/Material)
- Include realistic placeholder content
- Show proper spacing and typography
- Have a clean, modern aesthetic

Specify viewport size and device frame.""",
    "source": "AI Prompt Library — UI Prompts 2026",
    "usage": "UI 界面截图生成，适合快速原型展示和设计提案。"
})

prompts.append({
    "title": "Logo 概念设计",
    "prompt": """Generate logo design concepts for:

Brand: [品牌名称]
Industry: [行业]
Keywords: [关键词]
Style: [极简/几何/手绘/复古]
Color preferences: [颜色偏好]
Usage: [主要使用场景]

Generate 3 concepts, each with:
1. Concept description and symbolism
2. Typography recommendation
3. Color palette
4. When to use each variant
5. Where the logo should and shouldn't work""",
    "source": "AI Prompt Library — Creative Design 2026",
    "usage": "Logo 设计概念生成，含象征意义和配色方案。"
})

prompts.append({
    "title": "信息图表数据可视化",
    "prompt": """Create an infographic/data visualization concept for:

Data: [数据描述]
Story: [想传达的信息]
Audience: [目标读者]
Format: [社交媒体/报告/演示]

Design specifications:
1. Chart types (why each was chosen)
2. Color scheme (accessible, colorblind-friendly)
3. Typography hierarchy
4. Layout flow (reading order)
5. Key data callouts
6. Iconography suggestions
7. Source attribution

Describe the visual in detail so it can be recreated in any tool.""",
    "source": "AI Prompt Library / EverythingAI 2026",
    "usage": "信息图表概念设计，含图表类型选择和色彩方案。"
})

# ========================
# CATEGORY: Everyday Life (5 prompts)
# ========================

prompts.append({
    "title": "健身/运动计划生成",
    "prompt": """Create a workout plan for:

Goal: [增肌/减脂/力量/耐力]
Experience: [新手/中级/高级]
Days per week: [X天]
Equipment: [健身房/居家/徒手]
Time per session: [X分钟]
Injuries/limitations: [受伤或限制]

Provide:
1. Weekly split (which muscle groups on which days)
2. Exercises for each session with sets/reps
3. Progression plan (how to increase over time)
4. Warm-up and cool-down
5. Nutrition notes
6. Recovery recommendations""",
    "source": "AI Academy — Personal Life Prompts 2026",
    "usage": "个性化健身计划，含渐进超负荷设计。"
})

prompts.append({
    "title": "旅行行程规划",
    "prompt": """Plan a trip itinerary for:

Destination: [目的地]
Duration: [X天]
Travel style: [自由行/跟团/蜜月/家庭]
Budget: [预算范围]
Interests: [兴趣偏好]
Dietary needs: [饮食需求]

Generate:
1. Day-by-day itinerary with realistic timing
2. Must-see attractions vs hidden gems
3. Restaurant recommendations by cuisine
4. Transportation between locations
5. Estimated daily budget breakdown
6. Packing checklist for the climate
7. Backup plans for bad weather""",
    "source": "AI Academy / Promptitude 2026",
    "usage": "旅行行程规划，含每日节奏、美食推荐和备选方案。"
})

prompts.append({
    "title": "菜谱 / 饮食计划",
    "prompt": """Create a meal plan for:

Dietary preference: [素食/生酮/高蛋白/均衡]
Calorie target: [X卡路里/天]
Meals per day: [X餐]
Allergies: [过敏源]
Cuisine preference: [菜系]
Cooking skill: [初级/中级/高级]
Budget: [预算]

Provide:
1. Daily meal plan with portion sizes
2. Grocery shopping list (organized by category)
3. Prep-ahead strategies
4. Estimated nutrition breakdown
5. Substitution options for each meal
6. Time needed for preparation""",
    "source": "AI Academy — Life Prompts 2026",
    "usage": "饮食计划生成，含采购清单和备餐策略。"
})

prompts.append({
    "title": "第一封约会消息",
    "prompt": """Write a first message for a dating app:

Their profile says: [粘贴对方个人简介]
Shared interests: [共同兴趣]
My goal: [破冰/幽默/真诚展示]

The message should:
- Reference something specific from their profile
- Be conversational, not generic
- End with a question to keep the conversation going
- Be appropriate length (not too short, not too long)
- Reflect my authentic personality

Generate 3 variations with different approaches.""",
    "source": "Reddit / AI Academy — Creative Personal 2026",
    "usage": "生成个性化第一封约会消息，引用对方个人资料的具体内容。"
})

prompts.append({
    "title": "家居整理/收纳方案",
    "prompt": """Create an organization plan for:

Space: [房间/区域]
Current state: [描述现状]
Available storage: [现有收纳条件]
Items to organize: [物品类型]
Goal: [极简/功能/美观]
Time available: [X小时]

Provide:
1. Decluttering strategy (keep/donate/trash)
2. Zoning plan (what goes where)
3. Storage solutions (what to buy/what to DIY)
4. Maintenance routine (how to keep it organized)
5. Before/after process timeline
6. Budget estimate for materials""",
    "source": "AI Academy — Life & Personal 2026",
    "usage": "家居收纳整理方案，从断舍离到维护习惯。"
})

# ========================
# CATEGORY: Education & Teaching (5 prompts)
# ========================

prompts.append({
    "title": "教案 / 课程大纲设计",
    "prompt": """Design a course outline for:

Course title: [课程名]
Target students: [学生背景]
Duration: [总课时]
Level: [入门/中级/高级]
Learning objectives: [学习目标]
Delivery: [线上/线下/混合]

Structure:
1. Course description (1 paragraph)
2. Prerequisites
3. Module breakdown (each with: topics, time, learning objectives)
4. Assignments and assessments
5. Required resources
6. Grading rubric
7. Weekly schedule""",
    "source": "SurePrompts / AI Academy 2026",
    "usage": "课程大纲设计，含模块拆解和评分标准。"
})

prompts.append({
    "title": "考试题目生成",
    "prompt": """Generate exam questions for:

Subject: [科目]
Topic: [具体主题]
Question types: [选择题/简答/论述]
Difficulty: [简单/中等/困难]
Number of questions: [X]

For each question, provide:
1. The question
2. Correct answer
3. Distractors (for multiple choice)
4. Explanation of the correct answer
5. Reference to learning material

Ensure questions test understanding, not just recall.""",
    "source": "SurePrompts — Education 2026",
    "usage": "考试题目生成，含干扰项设计和答案解释。"
})

prompts.append({
    "title": "读书笔记结构化提取",
    "prompt": """Extract key insights from this book/article:

Title: [标题]
Full text: [粘贴全文]

Structure the notes:
1. Thesis (the main argument, 2-3 sentences)
2. Key concepts (5-7, each with definition and significance)
3. Supporting evidence (data, examples, case studies)
4. Counter-arguments the author addresses
5. My takeaways (how this applies to my work/life)
6. Questions it raised for me
7. Related works to read next""",
    "source": "AI Academy — Learning Prompts 2026",
    "usage": "从书籍或长文中提取结构化笔记，含批判性思考。"
})

prompts.append({
    "title": "即兴辩论/论点生成",
    "prompt": """Structure a debate argument for:

Topic: [辩论主题]
Position: [正方/反方]
Audience: [评委/观众]
Key constraints: [辩论时长/规则]

Generate:
1. Opening statement (clear position + 3 supporting points)
2. For each point: claim, evidence, reasoning
3. Anticipated counter-arguments and rebuttals
4. Closing statement (summary + call to decision)

Tone: persuasive but logical. Use evidence over emotion.""",
    "source": "AI Academy / SurePrompts 2026",
    "usage": "辩论准备，含论点构建和预期反论。"
})

# ========================
# CATEGORY: System-Level / Meta Prompts (6 prompts)
# ========================

prompts.append({
    "title": "System Prompt 编写 — 角色专家",
    "prompt": """Act as a [角色] with:

Expertise: [专业领域]
Experience: [经验年限]
Communication style: [语气]
Special skills: [特殊技能]

When responding:
- Demonstrate deep domain knowledge
- Use appropriate terminology
- Provide practical, actionable advice
- Acknowledge limitations of your knowledge
- Ask clarifying questions when needed
- Cite relevant examples from your "experience"

Stay in character throughout the conversation.""",
    "source": "Awesome ChatGPT Prompts / System Prompts 2026",
    "usage": "让 AI 扮演特定专家角色，设定语气、技能和沟通方式。"
})

prompts.append({
    "title": "多轮对话上下文维护",
    "prompt": """Maintain context across our conversation:

This is a multi-turn conversation about:
Topic: [对话主题]
Previous decisions made: [已做的决定]
Pending items: [待定事项]
My preferences: [已知偏好]

Rules:
- Reference previous exchanges when relevant
- Build on earlier conclusions
- Don't repeat what was already covered
- Track status of open items
- Summarize progress at key milestones

Update your understanding as the conversation evolves.""",
    "source": "Promptitude — Multi-Turn Best Practices 2026",
    "usage": "多轮对话中让 AI 记住上下文、避免重复、跟踪进度。"
})

prompts.append({
    "title": "提示词质量自评",
    "prompt": """Evaluate the quality of this prompt:

Prompt: [粘贴要评估的提示词]

Score each dimension (1-10):
1. Clarity — is the task unambiguous?
2. Specificity — are constraints and format defined?
3. Context — is enough background provided?
4. Actionability — can the AI act on it immediately?
5. Measurability — would you know if the output is good?

For scores below 7, suggest specific improvements.
Provide an improved version of the prompt.""",
    "source": "SurePrompts — Prompt Improvement 2026",
    "usage": "对自己写的提示词进行量化评估和改进。"
})

prompts.append({
    "title": "输出格式强制约束",
    "prompt": """Respond in the following format only:

Format: [JSON / Markdown table / CSV / XML / YAML]

Schema:
[定义确切的输出结构]

Rules:
- Do not include any text outside the specified format
- Do not include markdown code block wrappers
- Follow the schema exactly
- Use null for missing values, not "N/A" or empty strings
- Validate the output confirms to the schema before responding

If you cannot produce valid output in this format, respond with: {"error": "reason"}""",
    "source": "Google Cloud / Prompt Engineering Guide 2026",
    "usage": "强制 AI 按指定格式输出，适合程序化调用的场景。"
})

prompts.append({
    "title": "人物角色一致性检查",
    "prompt": """You are maintaining a consistent persona. Before each response:

1. Re-read your assigned persona definition
2. Check if the proposed response stays in character
3. Verify tone and vocabulary match the persona
4. Ensure knowledge boundaries are respected
5. Consider how this persona would handle the specific situation

If the response would break character, adjust it.
If the request is outside the persona's knowledge, say so in-character.""",
    "source": "Reddit / ChatGPT Prompt Genius 2026",
    "usage": "确保 AI 在多轮对话中始终保持在设定的角色中。"
})

prompts.append({
    "title": "JSON 输出 Schema 强制",
    "prompt": """You are a structured data generator. Given the following input, output ONLY valid JSON that conforms EXACTLY to this schema:

{
  "schema": {
    "field1": "type: string, required: true, description: ...",
    "field2": "type: number, required: true, constraints: 0-100",
    "field3": "type: array, items: object, required: false"
  }
}

Input: [输入内容]

RULES:
- Output ONLY the JSON object, no other text
- Do not wrap in ```json or any code fences
- All required fields must be present
- Use correct types (strings in quotes, numbers without)
- If a field is missing, use null, not "N/A"
- Validate the JSON is parseable before outputting""",
    "source": "Google Cloud / EverythingAI — Structured Output 2026",
    "usage": "强制输出严格符合 Schema 的 JSON，不含任何多余文字。"
})

# =============================================
# Write to file
# =============================================

counter = existing_count
with open(FILE, "a") as f:
    for p in prompts:
        if is_duplicate(p["title"], p["prompt"]):
            print(f"SKIP (duplicate): {p['title']}")
            continue
        counter += 1
        f.write(f"\n## {counter}. {p['title']}\n\n")
        f.write(f"**Prompt：**\n```\n{p['prompt']}\n```\n")
        f.write(f"> 来源：{p['source']}\n")
        f.write(f"> 用法：{p['usage']}\n\n")
        f.write("---\n")

# Count total in file
with open(FILE, "r") as f:
    all_content = f.read()
total_prompts = len(re.findall(r'^## \d+\.', all_content, re.MULTILINE))

print(f"\n{'='*50}")
print(f"✅ 本次新增: {counter} 个提示词")
print(f"📊 文件总计: {total_prompts} 个提示词")
print(f"{'='*50}")
