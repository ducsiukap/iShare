# Architecture & Directory Structure

Complete guide to the agent instructions directory structure and organization.

---

## Directory Tree

```
.agent-instructions/
│
├─ README.md
│  └─ Entry point for all agents
│     • 30-second quick start
│     • Phase selection flowchart
│     • Quick links to all resources
│     • Example tasks by phase
│     • Learning path (5 days)
│
├─ COMMON-RULES.md
│  └─ 10 universal rules for ALL agents
│     1. Output Language (English default)
│     2. Output Format (Markdown .md)
│     3. Temporary Directory (.agents/.[agent]/[phase]/)
│     4. Edit Confirmation (Ask before editing)
│     5. Format by Phase (Phase-specific standards)
│     6. Code Output Standards (Tests, docs, quality)
│     7. Documentation Requirements (Full documentation)
│     8. QA Before Delivery (Pre-delivery checklist)
│     9. Git Workflow (English commits, clear messages)
│     10. Communication Standards (Clear, structured)
│
├─ NAVIGATION.md
│  └─ Comprehensive index and navigation guide
│     • Phase selection decision tree
│     • Phase selection quick table
│     • How to use (4 steps)
│     • Full file index with read times
│     • Multi-phase task guidance
│     • Task type quick finder (21 types)
│     • Common questions answered
│     • Navigation shortcuts
│
├─ SETUP.md
│  └─ Setup guide for team leads
│     • Quick setup (15 minutes)
│     • Team onboarding checklist
│     • Team member onboarding guide
│     • Directory structure explanation
│     • Git configuration
│     • Workflow steps for each task
│     • Common setup issues & solutions
│     • Monitoring & feedback
│     • Advanced: customization options
│
├─ ARCHITECTURE.md
│  └─ This file - directory structure documentation
│     • Complete directory layout
│     • File descriptions and purposes
│     • Quick reference section
│     • How to navigate
│
└─ [phases]/
   │
   ├─ system_analysis/
   │  │
   │  └─ AGENT.md
   │     └─ System Analysis Phase Rules & Procedures
   │        • 4 Mandatory Rules
   │        • 6 Task Types with full procedures
   │        • Pre-delivery checklists
   │        • Recommended tools
   │        • Common mistakes to avoid
   │
   ├─ design/
   │  │
   │  └─ AGENT.md
   │     └─ Design Phase Rules & Procedures
   │        • 4 Mandatory Rules
   │        • 7 Task Types with procedures
   │        • Step-by-step workflows
   │        • Recommended tools
   │        • Common mistakes to avoid
   │
   └─ coding/
      │
      └─ AGENT.md
         └─ Coding Phase Rules & Procedures
            • 5 Mandatory Rules
            • 8 Task Types with procedures
            • Quality standards & metrics
            • Performance targets
            • Common mistakes to avoid
```

---

## Temporary Work Directory

```
.agents/
│
└─ .claude/                            # Agent-specific workspace
   │
   ├─ system_analysis/                 # SA phase drafts & research
   │  ├─ research.md
   │  ├─ architecture_v1.md
   │  ├─ architecture_v2.md
   │  ├─ diagrams/
   │  └─ notes/
   │
   ├─ design/                          # Design phase drafts & iterations
   │  ├─ wireframes_draft.md
   │  ├─ user_flows_v1.md
   │  ├─ user_flows_v2.md
   │  ├─ design_system_draft.md
   │  ├─ assets/
   │  └─ exports/
   │
   └─ coding/                          # Coding phase drafts & iterations
      ├─ implementation_plan.md
      ├─ test_plan.md
      ├─ refactoring_notes.md
      ├─ code_snippets/
      └─ performance_analysis.md

NOTE: .agents/ should be in .gitignore and NOT committed to git
      Temporary work stored here, final deliverables delivered to user
```

---

## File Descriptions

### Master Documentation Files

#### README.md (Entry Point)

- **Purpose:** Primary entry point for all users
- **Contains:** Quick start guide, phase overview, navigation links
- **Read time:** 10-15 minutes
- **When to read:** First time using instructions, need orientation
- **Next:** Read COMMON-RULES.md or go to your phase AGENT.md

#### COMMON-RULES.md (Critical)

- **Purpose:** Define 10 universal rules applying to ALL phases
- **Contains:** Rules 1-10 with detailed explanations and examples
- **Read time:** 15-20 minutes
- **When to read:** Before executing any task
- **Critical rules:** Output language (English), format (.md), temp storage, edit confirmation
- **Next:** Read phase-specific AGENT.md

#### NAVIGATION.md (Discovery)

- **Purpose:** Help users find exactly what they need
- **Contains:** Task type index, phase selection guide, learning paths
- **Read time:** 10-15 minutes
- **When to read:** When looking for a specific task type, unsure which phase
- **Features:** Task type tables with time estimates, multi-phase guidance
- **Next:** Go to specific phase or task type

#### SETUP.md (For Team Leads)

- **Purpose:** Guide for initial setup and team onboarding
- **Contains:** Quick setup steps, team onboarding guide, configuration
- **Read time:** 15 minutes (active setup), 30+ minutes (full team onboarding)
- **When to read:** Setting up for first time, adding team members
- **Includes:** Email template for team members, common issues & fixes
- **Next:** Share with team members, follow setup checklist

#### ARCHITECTURE.md (Structure Reference)

- **Purpose:** Understand directory structure and file organization
- **Contains:** Directory tree, file descriptions, quick reference
- **Read time:** 5 minutes (reference), 15 minutes (full understanding)
- **When to read:** Understanding overall structure, where to find things
- **Features:** Complete directory tree, file descriptions, purpose statements
- **Next:** Go to specific file or phase

### Phase-Specific Files

#### system_analysis/AGENT.md

- **Purpose:** Rules and procedures for System Analysis phase
- **Mandatory Rules:** 4 (Big picture, Documentation, Relationships, Validation)
- **Task Types:** 6 (Architecture, Requirements, Database, API, ADR, Performance)
- **Read time:** 20 minutes
- **When to read:** Executing system analysis tasks
- **Features:** Step-by-step procedures, pre-delivery checklists, examples
- **Next:** Execute your task type following the procedures

#### design/AGENT.md

- **Purpose:** Rules and procedures for Design phase
- **Mandatory Rules:** 4 (User-centric, Consistency, Accessibility, Documentation)
- **Task Types:** 7 (Wireframes, User flows, Design system, Prototype, Tokens, Responsive, Review)
- **Read time:** 20 minutes
- **When to read:** Executing design tasks
- **Features:** Detailed procedures, tools recommendations, accessibility guidelines
- **Next:** Execute your task type following the procedures

#### coding/AGENT.md

- **Purpose:** Rules and procedures for Coding phase
- **Mandatory Rules:** 5 (Quality, Tests >80%, Spec, Performance & Security, Documentation)
- **Task Types:** 8 (Feature, Bug fix, Code review, Optimization, Refactoring, Testing, Migration, API)
- **Read time:** 25 minutes
- **When to read:** Executing coding tasks
- **Features:** Quality standards, performance targets, detailed code examples
- **Next:** Execute your task type following the procedures

---

## Quick Reference

### File Sizes

| File                     | Size       | Type           |
| ------------------------ | ---------- | -------------- |
| COMMON-RULES.md          | 11 KB      | Critical       |
| README.md                | ~6 KB      | Navigation     |
| NAVIGATION.md            | 5.1 KB     | Reference      |
| SETUP.md                 | 6.3 KB     | Onboarding     |
| ARCHITECTURE.md          | 3 KB       | Structure      |
| system_analysis/AGENT.md | 4.9 KB     | Phase-specific |
| design/AGENT.md          | 3.9 KB     | Phase-specific |
| coding/AGENT.md          | 5.9 KB     | Phase-specific |
| **Total**                | **~50 KB** | Documentation  |

---

## Navigation Paths

### Path 1: First Time User (30 min)

1. Read README.md (this file's parent)
2. Skim COMMON-RULES.md (focus on Rules 1-4)
3. Identify your phase (use flowchart in README)
4. Read phase AGENT.md (20 min)
5. Ready to execute!

### Path 2: Looking for Specific Task (10 min)

1. Open NAVIGATION.md
2. Find your task type in quick finder tables
3. Go to phase AGENT.md
4. Follow task type procedure

### Path 3: Team Setup (1-2 hours)

1. Team lead reads SETUP.md (15 min)
2. Create directory structure (5 min)
3. Add .agents/ to .gitignore (2 min)
4. Share README.md with team
5. Team members: Follow Path 1 above

### Path 4: Understanding Structure (15 min)

1. Read this file (ARCHITECTURE.md)
2. Review directory tree
3. Understand .agents/ workspace
4. Check file descriptions

---

## Key Concepts

**Phase:** Logical grouping of work (System Analysis, Design, Coding)

**Task Type:** Specific type of work within a phase (21 types total)

**Mandatory Rules:** Non-negotiable requirements per phase (4-5 rules)

**Pre-delivery Checklist:** Quality gate before finishing (one per task type)

**Temporary Directory:** `.agents/.[agent-name]/[phase]/` for drafts and work-in-progress

**Final Deliverable:** Delivered to user, not stored in `.agents/`

---

## Critical Implementation Points

### Rule 1: Output Language

- Default: **English**
- Override: Only when task explicitly specifies different language
- Exception: Document language choice in comments

### Rule 2: Output Format

- Default: **Markdown (.md)**
- Alternatives: YAML (config), JSON (data), code (programming)
- Principle: Version-control friendly, searchable

### Rule 3: Temporary Storage

- Location: `.agents/.claude/[phase]/`
- Purpose: Drafts, research, iterations
- Not in git: Add `.agents/` to `.gitignore`

### Rule 4: Edit Confirmation

- **ASK** before editing (unless task says "edit/fix/modify/update")
- Workflow: Identify task → Ask → Receive confirmation → Proceed
- Exception keywords: "edit", "fix", "modify", "update", "sửa trực tiếp"

---

## Setup Checklist

- [ ] Directories created (`.agent-instructions/` and `.agents/.claude/`)
- [ ] All 9 files present
- [ ] `.agents/` added to `.gitignore`
- [ ] Team notified with README.md link
- [ ] First task in progress
- [ ] Pre-delivery checklist used

---

## Version Information

| Item         | Value            |
| ------------ | ---------------- |
| Version      | 1.0              |
| Created      | 2025-09-20       |
| Status       | Production Ready |
| Language     | 100% English     |
| Format       | 100% Markdown    |
| Last Updated | 2025-09-20       |

---

## Quick Links

- **Start here:** [README.md](./README.md)
- **All rules:** [COMMON-RULES.md](./COMMON-RULES.md)
- **Find task:** [NAVIGATION.md](./NAVIGATION.md)
- **Setup team:** [SETUP.md](./SETUP.md)
- **Your phase:**
  - [system_analysis/AGENT.md](./system_analysis/AGENT.md)
  - [design/AGENT.md](./design/AGENT.md)
  - [coding/AGENT.md](./coding/AGENT.md)

---

## 📝 Update History

These instructions are living documents. They may be updated as team practices evolve. Always check for the latest version in your repository.

| Date       | Version | Description     | Author | Status           |
| ---------- | ------- | --------------- | ------ | ---------------- |
| 2026-09-20 | 1.0.0   | Initial version | vduczz | Production Ready |

> For the latest updates, check your repository's `.agent-instructions/` directory.
