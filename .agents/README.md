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

- **Temporary storage only** — drafts, experiments, iterations
- **Not committed to git** — add `.agents/` to `.gitignore`
- **Final deliverables go outside** — deliver to user, not in `.agents/`
- **Workspace persists** — reuse for all your tasks

→ See [.agent-instructions/README.md](../.agent-instructions/README.md) (Workspace section) and COMMON-RULES Rule 3.
