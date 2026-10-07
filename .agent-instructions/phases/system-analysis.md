# System Analysis Phase

Goal: turn the product idea into requirements and design decisions that the design and coding phases can be built from directly. Nothing is designed visually and nothing is built in this phase. This is a graduation project: the business analysis is graded more strictly than the code, so every step is done carefully and every statement is traceable to a source.

Before you start, read [../COMMON-RULES.md](../COMMON-RULES.md). Then pick the skill that matches your task and follow its `SKILL.md`.

---

## Skills

| Task | Skill | Status |
|---|---|---|
| Interview the stakeholder, decompose modules and features, maintain the registers | [ba-interview](../skills/ba-interview/SKILL.md) | Active |
| Write or revise the Functional Requirement (FR) document of one module (7 gated steps) | [analyzing-functional-requirements](../skills/analyzing-functional-requirements/SKILL.md) | Active |
| Analyse dependencies between modules | `analyzing-dependencies` | Planned |
| Assess technical feasibility | `assessing-tech-feasibility` | Planned |
| Architecture, database schema, API contract, ADR, performance analysis | [technical-design](../skills/technical-design/SKILL.md) | Active (Phase 7 and 8) |

The previous System Requirement (SR) workflow (sr-author, sr-auditor, SR-DOCUMENT-RULES, sr-tools) is archived in [../_archive/sr-v1-2026-10/](../_archive/sr-v1-2026-10/). Do not use it.

---

## Pipeline for iShare

```
Idea draft ──► ba-interview ──► registers (ISS / QA / DEC / OPEN / glossary / module-registry)
                                   │
                                   ▼
                 analyzing-functional-requirements   (one module at a time, 7 steps,
                                   │                   stakeholder confirms every step)
                                   ▼
                                FR-Mxx.md
                                   │
          ┌────────────────────────┼──────────────────────────┐
          ▼                        ▼                          ▼
   dependencies /         NFR (Phase 7), data model      HMI / screen specs
   feasibility (planned)  (Phase 8, technical-design)    (design phase)
```

A requirement gap found in a later phase comes back to this phase for that scope; it is never patched inside a design document.

---

## Where things live

| What | Where |
|---|---|
| Stakeholder draft (read-only) | `docs/_temp/iShare_modules.md`, `iShare_specs_general.md` (requirement sources); `iShare_dev_priority.md` (reference only) |
| Stakeholder's reference sample for document structure | `docs/_temp/system_requirement_demo/` |
| Registers, intake, module registry (live) | `.agents/.claude/system_analysis/output/registers/`, `.../output/phase0-intake.md` |
| FR documents | `.agents/.claude/system_analysis/output/fr/FR-Mxx.md` (tool cache in `.../fr/.work/`) |
| Technical design outputs | `.agents/.claude/system_analysis/output/<architecture or data-model or api or adr or performance>/` |
| Approved documents | `docs/approved/` — promoted only after stakeholder approval |
| Backups of the instruction set | `.agents/.claude/system_analysis/backup/agent-instructions-<date>/` |

---

## Rules that apply to every skill in this phase

1. **Never invent requirements.** The idea draft and the stakeholder's recorded answers are the only sources of truth.
2. **Stay within the existing data.** Do not propose features or behaviour the sources never mention, unless their absence would stop a decided behaviour from working or touches permissions or data safety; then raise it as a point to consider and let the stakeholder decide.
3. **Everything is traceable** to the draft or to a register item (`ISS`, `QA`, `DEC`, `OPEN`).
4. **Unknown is not a guess.** A gap is confirmed with the stakeholder as the skill describes; answers go into the registers after the stakeholder approves the draft entry.
5. **Requirements describe behaviour, not design.** No layout, tables, fields or technology in a requirement.
6. **Gated work.** Skills with steps stop after every step and continue only on the stakeholder's explicit confirmation.

## Language

English is the default (COMMON-RULES Rule 1). **Exception (DEC-139):** FR documents are Vietnamese, with English kept only for necessary technical terms.

## Adding a skill

Create `skills/<name>/` with `SKILL.md` (front-matter `name` and `description`), `README.md` for the user, and the folders `input/`, `steps/`, `output/`, `tools/` as needed. Add one row to the table above and to [../README.md](../README.md), and add a pointer file `.claude/skills/<name>/SKILL.md` at the repository root so Claude Code discovers it. Do not copy rules between skills; link to the file that owns them.

## Next phase

When analysis is approved, continue with the [design phase](./design.md) (draft). Questions: see [../README.md](../README.md).
