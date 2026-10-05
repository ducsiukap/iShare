# System Analysis Phase

Goal: turn the product idea into requirements and design decisions that the design and coding phases can be built from directly. Nothing is designed visually and nothing is built in this phase.

This file is the **entry point** of the phase. Pick the role that matches your task, open its `AGENT.md`, and follow it. Every role file has the same shape (front-matter `name` and `description`, then rules and procedure), so any of them can also be registered as a skill without changing its content.

Before you start, read [../COMMON-RULES.md](../COMMON-RULES.md).

---

## Roles

| Task | Role | File | Status |
|---|---|---|---|
| Interview the stakeholder, decompose modules and features, maintain the registers | `ba-interview` | [roles/ba-interview/AGENT.md](./roles/ba-interview/AGENT.md) | Active |
| Write or revise the System Requirement (SR) document of one module | `sr-author` | [roles/sr-author/AGENT.md](./roles/sr-author/AGENT.md) | Active |
| Audit an SR document independently (never edits it; runs as passes P1/P2/P3 + MERGE, then VERIFY, then RELEASE verification after the stakeholder's decisions) | `sr-auditor` | [roles/sr-auditor/AGENT.md](./roles/sr-auditor/AGENT.md) | Active |
| Architecture, database schema, API contract, ADR, performance analysis | `technical-design` | [roles/technical-design/AGENT.md](./roles/technical-design/AGENT.md) | Active (used for Phase 7 and 8) |

Shared material used by more than one role lives in `shared/`:

| File | Content |
|---|---|
| [shared/SR-DOCUMENT-RULES.md](./shared/SR-DOCUMENT-RULES.md) | Single source of truth for SR documents: structure, ID scheme, Vietnamese EARS sentence templates, ownership, routing file, lifecycle, finding classes and severity, and the shared quality checklist (§10, used by both Author and Auditor) |
| [shared/templates/](./shared/templates/) | Fill-in files: SR, routing file, selfcheck, test cases, audit pass file, audit report, audit invocation prompt. Roles copy them instead of retyping |
| [shared/examples/](./shared/examples/) | Worked examples: one feature from source to SR, one audit finding, and Author/Auditor test cases that expose source ambiguity |
| [shared/sr-tools/](./shared/sr-tools/) | `inventory.py` (gather the sources of one module) and `check_sr.py` (automatic SR checks). Python 3 only |

---

## Pipeline for iShare

```
Idea draft ──► ba-interview ──► registers (ISS / QA / DEC / OPEN)
                                   │
                                   ▼
                    sr-author ⇄ sr-auditor   (one module at a time, max 2 audit rounds + 1 verify pass,
                                   │          every GAP raised to the stakeholder)
                                   ▼
                    ISH-SR-Mxx  +  ISH-RT-Mxx (routing)
                                   │
          ┌────────────────────────┼─────────────────────────┐
          ▼                        ▼                         ▼
   NFR (BA Phase 7)     Data model (BA Phase 8,       HMI / screen specs
                        technical-design)             (design phase)
```

- SR documents are written **now**; NFR and data-model work start afterwards and receive what each SR routes to them (routing sections R1 and R2).
- A requirement gap found in a later phase comes back to this phase for that scope; it is never patched inside a design document.

---

## Where things live

| What | Where |
|---|---|
| Stakeholder draft (read-only, cited as `DRAFT §x.y`) | `docs/_temp/iShare_specs_general.md`, `iShare_modules.md`, `iShare_dev_priority.md` |
| Registers, intake, module registry (live) | `.agents/.claude/system_analysis/output/registers/` and `.../output/phase0-intake.md` |
| SR documents, routing files, audit reports | `.agents/.claude/system_analysis/output/specs/` (`routing/`, `audit/`) |
| Technical design outputs | `.agents/.claude/system_analysis/output/<architecture or data-model or api or adr or performance>/` |
| Approved documents | `docs/approved/` — promoted only after stakeholder approval and a passed checklist |
| Backup of the instruction set before the 2026-10-04 restructure | `.agents/.claude/system_analysis/backup/agent-instructions-2026-10-04/` |

---

## Rules that apply to every role in this phase

1. **Never invent requirements.** The idea draft and the stakeholder's recorded answers are the only sources of truth.
2. **Everything is traceable** to `DRAFT §x.y` or to a register item (`ISS`, `QA`, `DEC`, `OPEN`).
3. **Unknown is not a guess.** An unknown becomes a question, an open item, or an explicit assumption that the stakeholder confirms.
4. **One issue per message** when asking the stakeholder, with options, consequences and a recommendation.
5. **Requirements describe behaviour, not design.** No layout, tables, fields or technology in a requirement.
6. **Think big picture first, document every decision, map dependencies, validate with the stakeholder.**

## Language

English is the default (COMMON-RULES Rule 1). **Exception (DEC-139):** SR documents and routing files are Vietnamese, with English kept only for necessary technical terms, and carry the marker `[Vietnamese Doc]`.

## Adding or changing a role

Create `roles/<name>/AGENT.md` with front-matter `name` and `description`, put anything reused by another role into `shared/`, and add one row to the role table above. Do not copy rules between roles; link to the file that owns them. If a role is also registered as an account skill, keep that skill a thin pointer to its `AGENT.md` so there is only one source of truth.

## Next phase

When analysis is approved, continue with the [design phase](../design/AGENT.md) (draft). Questions: see [../README.md](../README.md).
