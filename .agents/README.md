# Agent Workspaces

This directory contains temporary workspaces for agents.

## 📁 Structure

Each agent creates their own workspace:
```
.agents/
└── .[agent-name]/              # e.g., .claude, .gpt, .my-custom-agent
    ├── system_analysis/        # Phase 1: SA phase work
    ├── design/                 # Phase 2: Design phase work
    └── coding/                 # Phase 3: Coding phase work
```

## 🔗 Instructions & Rules

For complete instructions on phases, rules, and procedures:
→ [.agent-instructions/README.md](../.agent-instructions/README.md)

## ⚙️ Quick Setup

```bash
# Create your workspace (first time only)
mkdir -p .agents/.[agent-name]/{system_analysis,design,coding}
```

Replace `[agent-name]` with your identifier (e.g., claude, gpt, custom-agent).

## 📝 Important

- **Working storage** — drafts, experiments, iterations, and the System Analysis output
- **Committed to git** — `.agents/.claude/system_analysis/output/` (registers, FR documents) is the shared project record; only caches (`output/fr/.work/`) are ignored. Never add `.agents/` as a whole to `.gitignore`
- **Approved deliverables** are promoted to `docs/approved/`
- **Workspace persists** — reuse for all your tasks; other agents read and update the registers in `.agents/.claude/system_analysis/output/`, they do not create their own copy

→ See [.agent-instructions/README.md](../.agent-instructions/README.md) (Workspace section) and COMMON-RULES Rule 3.
