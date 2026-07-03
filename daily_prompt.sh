#!/bin/bash
# 每天定时收集热门 AI 提示词，追加到 prompt.md，自动 git 推送
# 由 openclaw cron 在 12:00 触发

PATH=/usr/local/bin:/usr/bin:/bin:/opt/homebrew/bin
cd /Users/tony/develop/openclaw/prompt

# 今天的日期作为标题
TODAY=$(date +%Y-%m-%d)

echo "📡 正在搜索热门 AI 提示词..."

# 我们用 openclaw agent 来搜索并更新 prompt.md
# 此脚本只负责 git 提交，实际搜索由 cron job 的 agentTurn 完成

exit 0
