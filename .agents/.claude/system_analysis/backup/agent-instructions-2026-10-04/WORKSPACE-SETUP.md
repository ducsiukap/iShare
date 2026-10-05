# Workspace Setup Guide for Agents

This guide helps **agents** create their own temporary workspace for drafts and intermediate work.

---

## 🚀 Quick Start (2 minutes)

Before starting any task, create your temporary workspace directory:

```bash
# Navigate to project root
cd /path/to/your/project

# Create your agent workspace
# Replace [agent-name] with your identifier (e.g., claude, gpt, custom-agent)
mkdir -p .agents/[agent-name]/{system_analysis,design,coding}
```

**Examples:**

```bash
# If you're Claude
mkdir -p .agents/.claude/{system_analysis,design,coding}

# If you're GPT
mkdir -p .agents/.gpt/{system_analysis,design,coding}

# If you're a custom agent
mkdir -p .agents/.my-custom-agent/{system_analysis,design,coding}
```

---

## 📁 Workspace Structure

Your workspace organizes temporary work by phase:

```
.agents/
└── .[agent-name]/                    # Your agent workspace
    ├── system_analysis/              # System Analysis phase work
    │   ├── research.md
    │   ├── draft_architecture.md
    │   ├── diagrams/
    │   └── notes/
    │
    ├── design/                       # Design phase work
    │   ├── wireframes_draft.md
    │   ├── user_flows.md
    │   ├── assets/
    │   └── exports/
    │
    └── coding/                       # Coding phase work
        ├── implementation_plan.md
        ├── test_plan.md
        ├── code_snippets/
        └── performance_analysis.md
```

---

## 📋 What Goes in Your Workspace?

**Temporary/Draft Work:**

- Research and notes
- Draft documents (v1, v2, v3)
- Sketches and experiments
- Intermediate outputs
- Test files and snippets
- Work-in-progress analyses

**DO NOT put in workspace:**

- Final deliverables (deliver to user, not in `.agents/`)
- Production code (belongs in main project)
- Approved documents (move to `.agent-instructions/` if applicable)

---

## 🔄 Workflow: From Workspace to Delivery

### Step 1: Work in Your Workspace

```bash
# Create drafts in your agent workspace
.agents/.[agent-name]/[phase]/draft_v1.md
.agents/.[agent-name]/[phase]/draft_v2.md
.agents/.[agent-name]/[phase]/draft_v3.md
```

### Step 2: Review with User

- Share final draft with user for feedback
- Get approval before final delivery

### Step 3: Deliver Final Version

```bash
# Move final approved version OUT of .agents/
# Deliver to user (not in .agents/)
final-deliverable.md  ← Delivered to user
```

### Step 4: Optional - Archive

```bash
# After approval, can optionally archive workspace
# But typically just leave .agents/ as-is for reference
```

---

## ⚙️ Git Configuration

**Important:** `.agents/` should NOT be committed to git.

```bash
# Add to .gitignore (at project root)
echo ".agents/" >> .gitignore

# Verify it's ignored
git status  # Should NOT show .agents/ or its contents
```

**Why?**

- Temporary work shouldn't clutter version history
- Each agent can have their own workspace without conflicts
- Keeps repository clean for production code only

---

## 📝 Naming Your Workspace

**Choose a name that identifies you:**

| Agent        | Folder Name | Path                 |
| ------------ | ----------- | -------------------- |
| Claude       | `.claude`   | `.agents/.claude/`   |
| GPT          | `.gpt`      | `.agents/.gpt/`      |
| Custom agent | `.my-agent` | `.agents/.my-agent/` |
| Your name    | `.alice`    | `.agents/.alice/`    |

**Guidelines:**

- Keep it short (1-3 words)
- Use lowercase with dots or hyphens
- Be consistent - always use the same name
- Avoid special characters

---

## ✅ Verification Checklist

After creating your workspace:

```bash
# Verify workspace exists
ls -la .agents/.[agent-name]/

# Verify subdirectories exist
ls -la .agents/.[agent-name]/{system_analysis,design,coding}

# Verify .gitignore has .agents/
grep ".agents/" .gitignore

# Verify git won't track .agents/
git status | grep -i agents  # Should return nothing
```

✅ **If all checks pass:** Your workspace is ready!

---

## 🎯 Examples

### Example 1: Claude Creating Workspace

```bash
cd /path/to/iShare
mkdir -p .agents/.claude/{system_analysis,design,coding}

# Verify
ls -la .agents/.claude/
```

**Result:**

```
.agents/
└── .claude/
    ├── system_analysis/
    ├── design/
    └── coding/
```

### Example 2: Working on a System Analysis Task

```bash
# Navigate to your SA workspace
cd .agents/.claude/system_analysis/

# Create draft
echo "# Architecture Analysis - v1" > architecture_v1.md

# Iterate
echo "# Architecture Analysis - v2" > architecture_v2.md

# Final version ready? Deliver to user (not in .agents/)
```

---

## 📌 Key Points

1. **Create workspace once** - Use the same `.[agent-name]/` for all your tasks
2. **Organize by phase** - Keep system_analysis, design, coding separate
3. **Draft freely** - Experiment without affecting production code
4. **Deliver outside `.agents/`** - Final deliverables go to user, not workspace
5. **Don't commit** - Add `.agents/` to `.gitignore`
6. **Reference for later** - Workspace stays for reference after approval

---

## ❓ Questions?

**"Do I need to create the workspace every time?"**
→ No, create it once. Reuse the same workspace for all tasks.

**"Can multiple agents share one workspace?"**
→ No, each agent should have their own `.[agent-name]/` directory.

**"What if my workspace gets messy?"**
→ That's fine! It's temporary work. Clean it up manually or just leave it.

**"Should I commit my workspace drafts?"**
→ No, `.agents/` should be in `.gitignore` so nothing is committed.

**"Where do I put final deliverables?"**
→ Deliver to user OUTSIDE of `.agents/`. Don't leave them in your workspace.

---

## 🚀 Next Steps

1. ✅ Create your workspace using the quick start above
2. ✅ Add `.agents/` to `.gitignore`
3. ✅ Read [README.md](./README.md) to identify your task phase
4. ✅ Read [COMMON-RULES.md](./COMMON-RULES.md) for universal rules
5. ✅ Read your phase-specific AGENT.md file
6. ✅ Start working in your workspace!

---

## 📝 Update History

These instructions are living documents. They may be updated as team practices evolve. Always check for the latest version in your repository.

| Date       | Version | Description     | Author | Status           |
| ---------- | ------- | --------------- | ------ | ---------------- |
| 2026-09-20 | 1.0.0   | Initial version | vduczz | Production Ready |

> For the latest updates, check your repository's `.agent-instructions/` directory.
