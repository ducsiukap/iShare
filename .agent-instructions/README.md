# Agent Instructions

The single entry point for any agent working on iShare. This directory tells an agent **which role to play, which rules apply, and where files go**.

---

## Quick start

1. Read [COMMON-RULES.md](./COMMON-RULES.md) — 10 rules for every agent and every phase.
2. Pick your phase (table below) and open its `AGENT.md`.
3. Inside **System Analysis**, pick a **role** (each role is one folder with one `AGENT.md`) and follow it.
4. Work in the agent workspace (see below); promote finished, approved documents to `docs/approved/`.

| Phase | Entry file | Use for | Status |
|---|---|---|---|
| System Analysis | [system_analysis/AGENT.md](./system_analysis/AGENT.md) | Interviews, registers, System Requirement documents, architecture, data model, API, ADR | **Active** |
| Design | [design/AGENT.md](./design/AGENT.md) | UI/UX: mockups, flows, design system, prototypes | Draft — not yet aligned with the current workflow |
| Coding | [coding/AGENT.md](./coding/AGENT.md) | Features, bug fixes, tests, refactoring, deployment | Draft — not yet aligned with the current workflow |

Not sure which phase? Writing or fixing code → Coding. Producing visual designs → Design. Anything about requirements, data, architecture or APIs → System Analysis.

---

## System Analysis roles

| Task | Role | File |
|---|---|---|
| Interview the stakeholder, maintain registers | `ba-interview` | [system_analysis/roles/ba-interview/AGENT.md](./system_analysis/roles/ba-interview/AGENT.md) |
| Write or revise one module's SR document | `sr-author` | [system_analysis/roles/sr-author/AGENT.md](./system_analysis/roles/sr-author/AGENT.md) |
| Audit an SR document (independent, never edits) | `sr-auditor` | [system_analysis/roles/sr-auditor/AGENT.md](./system_analysis/roles/sr-auditor/AGENT.md) |
| Architecture, database, API, ADR, performance | `technical-design` | [system_analysis/roles/technical-design/AGENT.md](./system_analysis/roles/technical-design/AGENT.md) |
| Rules shared by the SR roles | — | [system_analysis/shared/SR-DOCUMENT-RULES.md](./system_analysis/shared/SR-DOCUMENT-RULES.md) |

---

## Directory structure

```
.agent-instructions/
├── README.md                  ← this file (the only index)
├── COMMON-RULES.md            ← universal rules, incl. workspace and output locations
├── system_analysis/
│   ├── AGENT.md               ← phase entry: role table, pipeline, where things live
│   ├── shared/
│   │   ├── SR-DOCUMENT-RULES.md
│   │   ├── templates/         ← SR, routing, selfcheck, tests, audit partial/report, audit prompt
│   │   ├── examples/          ← worked examples (feature, audit finding, tests)
│   │   └── sr-tools/          ← inventory.py, check_sr.py
│   └── roles/
│       ├── ba-interview/AGENT.md
│       │   └── reference/legacy-feature-spec.md   ← superseded template, reference only
│       ├── sr-author/AGENT.md
│       ├── sr-auditor/AGENT.md
│       └── technical-design/AGENT.md
├── design/AGENT.md            ← draft
└── coding/AGENT.md            ← draft
```

Every role file starts with front-matter (`name`, `description`) and can be registered as an account skill unchanged. Keep any such skill a thin pointer to the role file so the repository stays the single source of truth.

---

## Workspace

Agents write working files in their own workspace, not in the project root:

```
.agents/.[agent-name]/            e.g. .agents/.claude/
└── system_analysis/output/       registers/, specs/, ... (see system_analysis/AGENT.md)
```

Create it once (`mkdir -p .agents/.claude/{system_analysis,design,coding}`), reuse it for every task, keep one workspace per agent, and follow the git rule in COMMON-RULES Rule 3. Approved documents move to `docs/approved/`; stakeholder drafts stay read-only in `docs/_temp/`.

---

## FAQ

**Which language do I write in?** English by default; System Requirement documents are Vietnamese (DEC-139) and carry the marker `[Vietnamese Doc]`. See COMMON-RULES Rule 1.

**May I edit a file directly?** Only if the task says so (edit, fix, update, sửa, cập nhật…). Otherwise ask first. See COMMON-RULES Rule 4.

**Where is the history of the previous layout?** `.agents/.claude/system_analysis/backup/agent-instructions-2026-10-04/` (the directory has no git history).
