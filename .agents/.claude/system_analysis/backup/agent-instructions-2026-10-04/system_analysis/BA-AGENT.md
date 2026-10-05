# Business Analysis Phase — Agent Rules & Procedures

This phase turns a product idea into validated, traceable requirements. Nothing is designed and nothing is built here.

---

## 🎯 Phase Overview

**Goal:** Produce a complete set of system specifications that the HMI/screen specification phase and the implementation phase can be built from directly.

**Pipeline position:**

```
Idea draft + summary
   └─► [1] BA interview ──► SPEC-*.md   (what the system must do)   ◄── this phase
          └─► [2] HMI / screen specs    (derived from the FRs)
                 └─► [3] Implementation
```

**When to use this phase:**

- Interviewing the stakeholder to gather and clarify product requirements
- Decomposing a product into modules and features
- Defining actors, roles and permissions
- Writing functional requirements, business rules, flows and acceptance criteria
- Defining non-functional requirements
- Resolving ambiguity and contradiction in an idea draft

**Deliverables:** interview registers + one specification file per feature, plus the shared spec files.

**Language:** every output file is written in **English**. The interview itself may be English or Vietnamese, in simple wording. **Exception (DEC-139):** System Requirement (SR) documents are written in Vietnamese — see *System Requirement documents* below.

---

## 📋 Mandatory Rules

The full protocol lives in → [BA-INTERVIEW-RULES.md](./BA-INTERVIEW-RULES.md). Read it before starting.

**Quick summary:**

1. **Never invent requirements.** The idea draft and the stakeholder's answers are the only sources of truth.
2. **Everything is traceable.** Every requirement carries a source: `DRAFT §x.y` or `QA-###`. A requirement with no source is deleted or turned into an open issue.
3. **Unknown ≠ guess.** An unknown becomes a question, an `OPEN-###`, or an explicit `ASM-###` that the stakeholder confirms. Never a silent assumption.
4. **Work from an Issue Queue.** On entering a scope, log every unclear point first, then ask **one issue per message** with real options and their consequences.
5. **No question limit.** Keep asking until the scope in focus is fully clear. Never stop early for efficiency.
6. **No spec writing while a Blocker issue is open** in that scope.
7. **Requirements describe behaviour, not design.** Precise enough to design a screen from, without prescribing layout, widgets or visuals — the HMI phase does that.
8. **Requirements are atomic and testable.** "The system shall …", one verifiable behaviour each. Banned words: fast, easy, user-friendly, modern, secure, optimal — replace with a measurable criterion or ask.

---

## 🔖 ID Conventions

| ID                 | Meaning                                         |
| ------------------ | ----------------------------------------------- |
| `ISS-###`          | Issue in the interview queue                    |
| `QA-###`           | Question and recorded answer                    |
| `ASM-###`          | Assumption, pending or confirmed                |
| `DEC-###`          | Decision, with options considered and rationale |
| `OPEN-###`         | Unresolved issue carried into a document        |
| `FR-<MOD>-###[.n]` | Functional requirement and sub-requirement      |
| `BR-<MOD>-###`     | Business rule                                   |
| `ERR-<MOD>-###`    | Error case                                      |
| `AC-<MOD>-###`     | Acceptance criterion                            |
| `NFR-<CAT>-###`    | Non-functional requirement                      |
| `ISH-SR-Mxx`       | System Requirement document of module Mxx       |
| `ISH-RT-Mxx`       | Routing file of module Mxx (items that are not functional requirements) |
| `ISH-Mxx-nnn[.k]`  | SR requirement (upper-level / lower-level), permanent |
| `OP-Mxx-nn`        | Temporary open point inside an SR (Appendix B)  |
| `AUD-Mxx-nn`       | Audit finding in an SR audit report             |

Module code: 3–5 uppercase letters (`AUTH`, `POST`, `SRCH`). IDs are permanent — never renumber, deprecate instead. SR documents use the `ISH-…` IDs above instead of `FR-<MOD>-###`; details in [SR-DOCUMENT-RULES.md](./SR-DOCUMENT-RULES.md) §2.

---

## 🗣 The 9-Phase Interview

| Phase | Scope                                                                                             |
| ----- | ------------------------------------------------------------------------------------------------- |
| 0     | Intake & gap analysis — read the draft, state your understanding, publish the initial Issue Queue |
| 1     | Business context — problem, users, goals, success metrics, constraints, out of scope              |
| 2     | Actors, roles & permissions — permission matrix                                                   |
| 3     | Module decomposition — module list with MoSCoW priority (**gate: approval**)                      |
| 4     | Feature decomposition per module (**gate: approval**)                                             |
| 5     | Feature deep dive — the main work, one feature at a time                                          |
| 6     | Cross-cutting concerns — auth, notifications, search, uploads, audit, i18n, AI features           |
| 7     | Non-functional requirements — each with a measurable target                                       |
| 8     | Data model & integrations                                                                         |
| 9     | Open-issue clearing round                                                                         |

**Loop for every scope:**

1. Build the Issue Queue (`ISS-###`, typed, severity Blocker → Major → Minor)
2. Ask one issue per message, with options + consequences + a recommendation
3. Record the answer as `QA-###`, restate it, close the issue
4. Append any new issue the answer created
5. When the queue is clear of Blocker/Major: playback the scope summary and get explicit `confirm` before moving on

---

## 📒 Registers (6, kept live)

| Register    | Purpose                                                                |
| ----------- | ---------------------------------------------------------------------- |
| Issue Queue | The working backlog of the interview                                   |
| QA Log      | Every question and its recorded answer — the trace source for most FRs |
| Open Issues | Unresolved items and what they block                                   |
| Assumptions | Proposed assumptions and their confirmation status                     |
| Decisions   | Decisions taken, options considered, rationale                         |
| Glossary    | Every domain term and acronym, as the stakeholder defines it           |

These are not optional. The QA Log in particular is what makes the specs verifiable — without it, traceability is unprovable.

---

## 📄 Output Files

One file per feature, plus the shared files.

| File                                 | Content                                                                                 |
| ------------------------------------ | --------------------------------------------------------------------------------------- |
| `SPEC-000-index.md`                  | Product overview, module map, feature index, ID conventions, global traceability matrix |
| `SPEC-001-glossary.md`               | Glossary and abbreviations                                                              |
| `SPEC-002-actors-and-permissions.md` | Actors, roles, permission matrix                                                        |
| `SPEC-003-data-model.md`             | Entities, attributes, relationships, state machines                                     |
| `SPEC-004-nfr.md`                    | Non-functional requirements                                                             |
| `SPEC-005-open-issues.md`            | Open issues, assumptions, decisions                                                     |
| `SPEC-<MOD>-<NN>-<feature-slug>.md`  | One per feature — the main deliverable                                                  |

Every feature spec follows the standard template (metadata header · ToC · purpose & scope · abbreviations · actors · assumptions · functional requirements with sub-requirements · business rules · data specification · flows · states · permissions · error handling · applicable NFRs · acceptance criteria · open issues · traceability matrix · revision history). Full template in [BA-INTERVIEW-RULES.md](./BA-INTERVIEW-RULES.md).

Each traceability matrix includes a **Notes for HMI spec** column — what the screen specification will need from this feature, expressed behaviourally.

---

## 📘 System Requirement (SR) documents (DEC-139)

Functional requirements are written **now**, one Vietnamese SR document per module (`ISH-SR-Mxx`), from the registers and the idea draft. Phase 7 (NFR) and Phase 8 (data model) follow later and receive the items the SR routes to them.

| Item | Where |
| ---- | ----- |
| Normative rules (format, IDs, sentence templates, ownership, routing, lifecycle) | [SR-DOCUMENT-RULES.md](./SR-DOCUMENT-RULES.md) |
| Output (SR, routing file, audit reports) | `.agents/.claude/system_analysis/output/specs/` (`routing/`, `audit/`) |
| Author agent skill | [skills/drafting-ishare-sr-module/SKILL.md](./skills/drafting-ishare-sr-module/SKILL.md) (writes and revises the SR; never audits) |
| Auditor agent skill | to be added under `skills/`; an independent agent that only audits and never edits |

Pipeline per module: Author drafts → Auditor audits (source-to-requirement coverage matrix + rule checklist) → Author fixes → at most 2 rounds, then the stakeholder decides. Gaps, ambiguities and suggestions are raised to the stakeholder one at a time and recorded in the registers. First run is a pilot on one module.

---

## 🗂 File Storage & Promotion

```
iShare/docs/
├── _temp/
│   ├── specs/                # drafts, freely rewritten
│   └── registers/            # issue-queue, qa-log, open-issues,
│                             # assumptions, decisions, glossary
└── approved/
    └── specs/                # promoted after approval — the base for the HMI phase
```

A file moves to `approved/` only when its checklist passes and the stakeholder confirms. Files in `approved/` change only through a new version plus a revision-history entry, never a silent edit.

---

## ✅ Phase Exit Gate

- [ ] All 9 phases completed; no Blocker issue open
- [ ] Every FR has a source (`DRAFT §` or `QA-###`) and is atomic and testable
- [ ] No banned vague words anywhere in the specs
- [ ] Every FR covered by at least one acceptance criterion
- [ ] Every flow covers happy path, alternate and exception paths
- [ ] Priorities assigned (MoSCoW); no conflicting requirements
- [ ] Every assumption confirmed, or accepted as a documented open issue
- [ ] Permission matrix reviewed and approved
- [ ] All acronyms in the glossary; every file has a working ToC
- [ ] Every file is valid Markdown, in English
- [ ] _Notes for HMI spec_ complete for every feature
- [ ] Stakeholder approval recorded; specs promoted to `approved/specs/`

---

## Recommended Tools

- **Markdown** — all specification files and registers
- **Mermaid** — only where a flow has real branching; linear flows stay as step tables
- **Spreadsheet** — optional alternative for the registers

---

## Phase Navigation

**Next:** HMI / screen specification, derived from the functional requirements and the _Notes for HMI spec_ lists. (Rules for that phase to be defined.)

**If a later phase finds a requirement gap:** it comes back here for that scope only — it is never patched inside a design document.

**Before you start:** read [COMMON-RULES.md](../COMMON-RULES.md)

**Detailed rules:** [BA-INTERVIEW-RULES.md](./BA-INTERVIEW-RULES.md)
