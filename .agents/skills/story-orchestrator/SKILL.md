---
name: story-orchestrator
description: Coordinate STory development across specialist agents for multi-part implementation or review; ordinary questions need no delegation.
---

# story-orchestrator

Read AGENTS.md and docs/HARNESS.md from the repository root. Check docs/plans/goal-proposal.md: the first multi-agent run is pending user discussion and authorization. Environment setup alone must not launch agents or create a goal.
After authorization, choose only relevant specialists from .codex/agents/. Assign objective, owned files, dependencies and acceptance criteria. Keep shared files and integration with the main agent. Maximum concurrency follows the runtime; current session supports main plus three workers. Define four roles but schedule them as needed.
Use native custom-agent selection if exposed. If the tool only accepts a task name and prompt, read the TOML and pass its developer instructions plus skill path explicitly; this is role prompting, not proof of native registration or sandbox enforcement. State that distinction. Never invent TeamCreate/TaskCreate tools.
Record decisions and evidence in docs/plans/. Run incremental independent QA after meaningful changes, then npm run verify and relevant browser checks. Stop when the agreed criteria are met; unresolved external dependencies require an honest report. Do not enable /goal, scheduled runs or model spending merely because this skill is loaded.
