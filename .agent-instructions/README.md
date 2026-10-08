# Agent Instructions

The single entry point for any agent working on iShare. This directory tells an agent **which phase it is in, which skill to use, which rules apply, and where files go**.

---

## Quick start

1. Read [COMMON-RULES.md](./COMMON-RULES.md) — rules for every agent and every phase.
2. Open the file of your phase in [phases/](./phases/).
3. Pick the skill for your task and follow its `SKILL.md`. Each skill also has a `README.md` for the user.
4. Work in the agent workspace (see below); promote finished, approved documents to `docs/approved/`.

| Phase | Entry file | Use for | Status |
|---|---|---|---|
| System Analysis | [phases/system-analysis.md](./phases/system-analysis.md) | Interviews, registers, Functional Requirement documents, architecture, data model, API, ADR | **Active** |
| Design | [phases/design.md](./phases/design.md) | UI/UX: mockups, flows, design system, prototypes | Draft — not yet aligned with the current workflow |
| Coding | [phases/coding.md](./phases/coding.md) | Features, bug fixes, tests, refactoring, deployment | Draft — not yet aligned with the current workflow |

Not sure which phase? Writing or fixing code → Coding. Producing visual designs → Design. Anything about requirements, data, architecture or APIs → System Analysis.

---

## Skills

| Task | Skill | Phase |
|---|---|---|
| Interview the stakeholder, maintain registers | [ba-interview](./skills/ba-interview/SKILL.md) | System Analysis |
| Write or revise one module's FR document (7 gated steps) | [analyzing-functional-requirements](./skills/analyzing-functional-requirements/SKILL.md) · [user guide](./skills/analyzing-functional-requirements/README.md) | System Analysis |
| Architecture, database, API, ADR, performance | [technical-design](./skills/technical-design/SKILL.md) | System Analysis (Phase 7, 8) |

Planned: `analyzing-dependencies`, `assessing-tech-feasibility`.

---

## Directory structure

```
.agent-instructions/
├── README.md            ← this file (the only index)
├── COMMON-RULES.md      ← universal rules, incl. workspace and output locations
├── phases/              ← one file per phase: goal, which skills, in which order
│   ├── system-analysis.md
│   ├── design.md        ← draft
│   └── coding.md        ← draft
├── skills/              ← one folder per skill: SKILL.md, README.md, input/, steps/, output/, tools/
│   ├── ba-interview/
│   ├── analyzing-functional-requirements/
│   └── technical-design/
```

## How other tools find this directory

- `AGENTS.md` and `CLAUDE.md` at the repository root point here.
- `.claude/skills/<name>/SKILL.md` at the repository root are **pointer files only**, so Claude Code discovers the skills. The real content lives in `skills/` here. Never edit a pointer's body; edit the skill.

---

## Workspace

Agents write working files in their own workspace, not in the project root:

```
.agents/.[agent-name]/            e.g. .agents/.claude/
└── system_analysis/output/       registers/, fr/, ... (see phases/system-analysis.md)
```

Create it once (`mkdir -p .agents/.claude/{system_analysis,design,coding}`), reuse it for every task, keep one workspace per agent, and follow the git rule in COMMON-RULES Rule 3. Approved documents move to `docs/approved/`; stakeholder drafts stay read-only in `docs/_temp/`.

---

## FAQ

**Which language do I write in?** English by default; FR documents are Vietnamese (DEC-139). See COMMON-RULES Rule 1.

**May I edit a file directly?** Only if the task says so (edit, fix, update, sửa, cập nhật…). Otherwise ask first. See COMMON-RULES Rule 4.

**Where is the history of previous layouts?** In git history only. The old SR workflow and the earlier backups were deleted on 2026-10-08.
