# Legacy: per-feature SPEC template, quality gate and ID scheme

> **LEGACY — superseded by the System Requirement (SR) documents (DEC-139, QA-265).** Functional requirements are now written per module as `ISH-SR-Mxx` (Vietnamese) by [sr-author](../../sr-author/AGENT.md) and audited by [sr-auditor](../../sr-auditor/AGENT.md); see [SR-DOCUMENT-RULES.md](../../../shared/SR-DOCUMENT-RULES.md). This file is kept for reference only. **Do not use it for new work** unless the stakeholder explicitly asks.
> The shared files `SPEC-000` … `SPEC-005` (index, glossary, actors and permissions, data model, NFR, open issues) are still planned for later phases and are listed in [../AGENT.md](../AGENT.md) §6, not here.

## A. Deliverables and ID scheme (legacy per-feature files)

When the interview is done, produce the following **Markdown (.md) files, written in English**. Generate **one file per message**, then wait for stakeholder review/approval before the next one.

> **SR exception (DEC-139):** functional requirements are delivered as one System Requirement document per module (`ISH-SR-Mxx`, Vietnamese) plus a routing file (`ISH-RT-Mxx`), stored under `.agents/.claude/system_analysis/output/specs/`, following [SR-DOCUMENT-RULES.md](../../../shared/SR-DOCUMENT-RULES.md). They take the place of the per-feature `SPEC-<MOD>-<NN>-<feature-slug>.md` files and of the `FR-<MOD>-<NNN>` ID scheme below. The shared files `SPEC-000` … `SPEC-005` are not changed by this decision.

**File set**

| File | Content |
|---|---|
| `SPEC-<MOD>-<NN>-<feature-slug>.md` | **One file per feature** — the main deliverable |

**ID conventions**

- Module code: 3–5 uppercase letters, e.g. `AUTH`, `POST`, `SRCH`.
- Functional requirement: `FR-<MOD>-<NNN>`; sub-requirement: `FR-<MOD>-<NNN>.<n>` (nest further only if truly needed).
- Business rule `BR-<MOD>-<NNN>` · Error `ERR-<MOD>-<NNN>` · Acceptance criterion `AC-<MOD>-<NNN>` · NFR `NFR-<CATEGORY>-<NNN>`.
- IDs are **permanent**. Never renumber; deprecate instead.
- SR documents use the `ISH-` IDs defined in SR-DOCUMENT-RULES.md §2 (for example `ISH-M05-004.1`) instead of the `FR-<MOD>-<NNN>` scheme.

---

## B. Per-feature SPEC file template

Every feature spec file must follow this structure exactly:

```
# <Feature Name> — System Specification

| Field | Value |
|---|---|
| Document ID | SPEC-<MOD>-<NN> |
| Module | <module name> |
| Version | 0.1 |
| Status | Draft / Reviewed / Approved |
| Date | <YYYY-MM-DD> |
| Source documents | Idea draft §…, QA-### |

## Table of Contents
<linked ToC covering every section below>

## 1. Purpose and Scope
### 1.1 Purpose
### 1.2 In Scope
### 1.3 Out of Scope
### 1.4 Related Documents

## 2. Abbreviations and Definitions
| Term / Abbreviation | Meaning |

## 3. Actors and Roles
| Actor | Description | Involvement in this feature |

## 4. Assumptions, Dependencies and Constraints
(reference ASM-### / DEC-###; dependencies on other feature IDs)

## 5. Functional Requirements
### 5.1 Requirement Summary
| ID | Requirement (short) | Priority | Source |
### 5.2 Detailed Requirements
For each FR:
**FR-<MOD>-<NNN> — <title>**
- Description: The system shall …
- Priority: Must / Should / Could
- Actor(s):
- Trigger:
- Pre-conditions:
- Post-conditions:
- Sub-requirements: FR-<MOD>-<NNN>.1 … (each one atomic and testable)
- Related rules: BR-…, Errors: ERR-…
- Source: DRAFT §… / QA-###

## 6. Business Rules
| ID | Rule | Applies to FR | Source |

## 7. Data Specification
| Field | Type | Mandatory | Constraints / Validation | Default | Read by | Written by | Error on invalid |

## 8. Process Flows
### 8.1 Main Flow
| Step | Actor | Action | System Response | Next |
### 8.2 Alternate Flows
### 8.3 Exception Flows
(Add a Mermaid diagram only when the flow has real branching; skip it for linear flows.)

## 9. States and Transitions
(state list + transition table: from → to, trigger, allowed role, side effects. Omit section if not applicable and say so.)

## 10. Permissions
| Capability | Role A | Role B | Guest |

## 11. Error Handling
| ID | Condition | System behaviour | Message intent (text, not UI copy) | Recovery |

## 12. Applicable Non-Functional Requirements
(reference NFR-### from SPEC-004, plus feature-specific targets)

## 13. Acceptance Criteria
| ID | Given | When | Then | Covers FR |

## 14. Open Issues
| ID | Issue | Impact | Owner | Status |

## 15. Traceability Matrix
| FR ID | Source (draft §/QA-###) | Business goal | AC IDs | Notes for HMI/screen spec |

## 16. Revision History
| Version | Date | Author | Change |
```

Rules for filling it:

- If a section does not apply, keep the heading and write `Not applicable — <one line reason>`. Never delete a heading.
- The **"Notes for HMI/screen spec"** column is where you flag what the screen designer must decide later (e.g. "list must expose status + author + timestamp; layout TBD"). Keep it behavioural.
- Do not put UI wording, colours, component names, or layout in any FR.

---

## C. Quality gate for per-feature SPEC files

Before you hand any file, self-check it and report the result at the end of the message:

- [ ] Every FR has a Source, and the source really says that.
- [ ] No requirement contains an invented number, limit, name or rule.
- [ ] Every FR is atomic and testable; no banned vague words.
- [ ] Every FR is covered by at least one acceptance criterion.
- [ ] Every acronym used in the file appears in Section 2.
- [ ] ToC matches the actual headings.
- [ ] No `TBD` outside Section 14; every `TBD` has an `OPEN-###`.
- [ ] Cross-references to other feature IDs resolve to files that exist or are planned.
- [ ] File is valid Markdown and entirely in English.

---

## D. Exit-gate items that applied only to per-feature SPEC files

- [ ] Every file has a working ToC.
- [ ] _Notes for HMI spec_ complete for every feature.
