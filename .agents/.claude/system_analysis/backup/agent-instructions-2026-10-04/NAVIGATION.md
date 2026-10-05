# Navigation Guide

Use this document to find exactly what you need and navigate the agent instructions.

Use this document to find exactly what you need.

---

## 🎯 Phase Selection Decision Tree

```
START: What does your task involve?

1. Are you writing, fixing, testing, or deploying code?
   YES → Go to CODING phase
   NO  ↓

2. Are you creating visual designs, mockups, user flows?
   YES → Go to DESIGN phase
   NO  ↓

3. Are you analyzing, designing, or planning?
   YES → Go to SYSTEM_ANALYSIS phase
   NO  ↓

NOT SURE? → Read the Phase Selection table below
```

---

## Phase Selection Quick Table

| Phase | Focus | Best For | Examples |
|-------|-------|----------|----------|
| 🔍 **System Analysis** | Understanding, planning, designing | Thinking before building | Architecture analysis, requirements, database design, API specs |
| 🎨 **Design** | Visual creation, UX flows | Making it look good | Wireframes, mockups, user flows, design systems |
| 💻 **Coding** | Implementation, testing, deployment | Building it | Features, bug fixes, tests, refactoring, deployments |

---

## How to Use These Instructions (4 Steps)

### Step 1: Identify Your Phase
Use the decision tree above to determine which phase applies to your task.

### Step 2: Go to Phase-Specific File
Navigate to:
- System Analysis: [system_analysis/AGENT.md](./system_analysis/AGENT.md)
- Design: [design/AGENT.md](./design/AGENT.md)
- Coding: [coding/AGENT.md](./coding/AGENT.md)

### Step 3: Follow Mandatory Rules
Each phase has 4-5 mandatory rules. Read and understand them completely before starting.

### Step 4: Execute Task Following Procedures
Follow the step-by-step procedures and use pre-delivery checklists before finishing.

---

## 📚 Full File Index

### Master Navigation Files

| File | Purpose | Read Time | Best For |
|------|---------|-----------|----------|
| [README.md](./README.md) | Entry point with 30-second quick start | 5 min | First-time users |
| [COMMON-RULES.md](./COMMON-RULES.md) | 10 universal rules for all agents | 15 min | Understanding core principles |
| [README.md](./README.md) | Workflow overview and phase description | 10 min | Learning the structure |
| [INDEX.md](./INDEX.md) | This file - comprehensive index | 10 min | Finding what you need |
| [SETUP.md](./SETUP.md) | Setup guide for team leads | 15 min | Installing/onboarding |
| [STRUCTURE.txt](./STRUCTURE.txt) | Visual file tree structure | 5 min | Understanding organization |

### Phase-Specific Files

| File | Phase | Rules | Task Types | Read Time |
|------|-------|-------|------------|-----------|
| [system_analysis/AGENT.md](./system_analysis/AGENT.md) | 🔍 System Analysis | 4 mandatory | 6 types | 20 min |
| [design/AGENT.md](./design/AGENT.md) | 🎨 Design | 4 mandatory | 7 types | 20 min |
| [coding/AGENT.md](./coding/AGENT.md) | 💻 Coding | 5 mandatory | 8 types | 25 min |

---

## Multi-Phase Task Guidance

### What if my task spans multiple phases?

**Example 1: Implement a new feature from scratch**
```
Phase 1: System Analysis (1-2 hours)
  └─ Understand requirements
  └─ Design database schema
  └─ Plan API contract

Phase 2: Design (2-3 hours)
  └─ Create UI mockups
  └─ Design user flows
  └─ Create component specifications

Phase 3: Coding (4-6 hours)
  └─ Implement backend
  └─ Implement frontend
  └─ Write tests
  └─ Deploy
```

**How to manage:**
1. Complete Phase 1 fully → Deliver results
2. Get approval → Move to Phase 2
3. Complete Phase 2 fully → Deliver results
4. Get approval → Move to Phase 3
5. Complete Phase 3 fully → Deploy

---

## Task Type Quick Finder

### System Analysis Task Types (6)

1. **System Architecture Analysis**
   - Input: Existing system, improvement goals
   - Output: Architecture diagram, recommendations
   - Time: 4-6 hours

2. **Requirements & Use Cases**
   - Input: Business need, stakeholder feedback
   - Output: User stories, use case diagram, acceptance criteria
   - Time: 3-5 hours

3. **Database Schema Design**
   - Input: Requirements, business rules
   - Output: ER diagram, DDL script, index strategy
   - Time: 3-4 hours

4. **API Contract Design**
   - Input: Feature requirements, data models
   - Output: OpenAPI spec, examples, error handling
   - Time: 2-3 hours

5. **Architecture Decision Record (ADR)**
   - Input: Decision to be made, alternatives
   - Output: Decision statement, rationale, trade-offs
   - Time: 2-3 hours

6. **Performance & Scalability Analysis**
   - Input: Current system, growth projections
   - Output: Bottleneck analysis, optimization plan, metrics
   - Time: 4-6 hours

**File:** [system_analysis/AGENT.md](./system_analysis/AGENT.md)

---

### Design Task Types (7)

1. **UI Mockup & Wireframe**
   - Steps: Wireframe → Mockup → Annotate → Responsive variants
   - Deliverable: Figma file with components
   - Time: 3-5 hours

2. **User Flow & Interaction**
   - Steps: Happy path → Alternative flows → State designs → Transitions
   - Deliverable: Flow diagram, interaction specifications
   - Time: 2-4 hours

3. **Design System**
   - Steps: Principles → Colors → Typography → Spacing → Components
   - Deliverable: Figma component library, documentation
   - Time: 8-12 hours

4. **Prototype & User Testing**
   - Steps: Create → Plan test → Run with users → Iterate
   - Deliverable: Interactive prototype, test report
   - Time: 6-8 hours

5. **Design Tokens & Style Guide**
   - Steps: Extract decisions → Create structure → Export → Distribute
   - Deliverable: Token file, style guide documentation
   - Time: 4-6 hours

6. **Responsive Design**
   - Steps: Define breakpoints → Design layouts → Test across devices
   - Deliverable: Mockups for 3+ breakpoints
   - Time: 3-4 hours

7. **Design Review & Handoff**
   - Steps: Self-review → Team review → Prepare spec → Export
   - Deliverable: Approved design, dev handoff spec
   - Time: 2-3 hours

**File:** [design/AGENT.md](./design/AGENT.md)

---

### Coding Task Types (8)

1. **Feature Implementation**
   - Process: Spec → Tasks → Tests → Code → Review → PR → Deploy
   - Quality: >80% test coverage, passes all tests
   - Time: 4-8 hours

2. **Bug Fix**
   - Process: Reproduce → Root cause → Fix → Regression test → Verify
   - Quality: All tests pass, no new issues
   - Time: 1-3 hours

3. **Code Review**
   - Process: Read PR → Coverage → Quality → Performance → Security → Feedback
   - Output: Detailed review with suggestions
   - Time: 1-2 hours

4. **Performance Optimization**
   - Process: Measure → Identify bottlenecks → Implement → Measure → Validate
   - Quality: Measurable improvement, no regressions
   - Time: 3-6 hours

5. **Refactoring**
   - Process: Understand → Write tests → Refactor → Keep tests green → Review
   - Quality: 100% tests passing, improved metrics
   - Time: 3-5 hours

6. **Testing**
   - Process: Plan strategy → Unit → Integration → E2E → Edge cases
   - Quality: >80% coverage, documented edge cases
   - Time: 3-6 hours

7. **Database Migration**
   - Process: Plan → Write up migration → Write down → Data handling → Test
   - Quality: Zero data loss, rollback verified
   - Time: 4-8 hours

8. **API Implementation**
   - Process: Design endpoint → Implement → Validation → Errors → Test → Document
   - Quality: Complete documentation, >90% coverage
   - Time: 3-5 hours

**File:** [coding/AGENT.md](./coding/AGENT.md)

---

## 10 Common Rules Reference

| # | Rule | Key Point | Exception |
|---|------|-----------|-----------|
| 1 | Output Language | English default | If task specifies different language |
| 2 | Output Format | Markdown (.md) | Use appropriate alt (JSON, YAML, code) |
| 3 | Temp Storage | `.agents/.[agent]/[phase]/` | Deliverables go to user |
| 4 | Edit Confirmation | Ask before editing | If task says "edit/modify/fix" |
| 5 | Format by Phase | Phase-specific standards | Always follow phase format rules |
| 6 | Code Standards | Tests, docs, quality | Required for all code output |
| 7 | Documentation | Purpose, usage, examples | Required for all deliverables |
| 8 | QA Checklist | Pre-delivery verification | Non-negotiable gate |
| 9 | Git Workflow | English commits, clear messages | Standard git practices |
| 10 | Communication | Clear, structured, checkpoints | Especially for multi-phase tasks |

**Full details:** [COMMON-RULES.md](./COMMON-RULES.md)

---

## Learning Paths

### Path A: Quick Start (1 hour)
1. Read [README.md](./README.md) - 5 min
2. Skim [COMMON-RULES.md](./COMMON-RULES.md) - 10 min
3. Read your phase AGENT.md - 20 min
4. Review task type procedures - 15 min
5. Execute your first task - Ongoing

### Path B: Thorough Learning (3 hours)
1. Read [README.md](./README.md) - 10 min
2. Read [COMMON-RULES.md](./COMMON-RULES.md) completely - 20 min
3. Read all 3 phase AGENT.md files - 60 min
4. Study SETUP.md and STRUCTURE.txt - 15 min
5. Practice with first task - 30+ min
6. Get feedback from team lead - Ongoing

### Path C: Team Onboarding (Full day)
1. Team lead reads [SETUP.md](./SETUP.md) - 30 min
2. Team lead sets up directory structure - 30 min
3. Team lead explains phases to team - 30 min
4. Individual team members follow Path B - 3 hours
5. Team reviews first deliverables - 1 hour
6. Iterate and refine processes - Ongoing

---

## Common Questions Answered

### "How do I know which phase?"
→ Use the Phase Selection Decision Tree at the top of this document

### "What if I'm not sure?"
→ Read the phase AGENT.md files for examples of task types

### "Can I skip the Common Rules?"
→ No. Rules 1-4 are critical. See [COMMON-RULES.md](./COMMON-RULES.md)

### "What's the temp directory structure?"
→ `.agents/.claude/[system_analysis|design|coding]/` - See [SETUP.md](./SETUP.md)

### "Should I ask for confirmation?"
→ Yes, unless the task says "edit", "fix", "modify", "update". See Rule 4 in [COMMON-RULES.md](./COMMON-RULES.md)

### "What format should I output?"
→ English + Markdown (.md) by default. See [COMMON-RULES.md](./COMMON-RULES.md) Rules 1-2

### "How long does each task type take?"
→ Check the task type tables above, time estimates included

### "Do we commit .agents/ to git?"
→ No! Add to .gitignore. See [SETUP.md](./SETUP.md)

---

## Navigation Shortcuts

**By Role:**
- 👨‍💼 **Team Lead** → [SETUP.md](./SETUP.md)
- 🔍 **System Analyst** → [system_analysis/AGENT.md](./system_analysis/AGENT.md)
- 🎨 **Designer** → [design/AGENT.md](./design/AGENT.md)
- 💻 **Developer** → [coding/AGENT.md](./coding/AGENT.md)
- ❓ **First time?** → [README.md](./README.md)

**By Task:**
- "I don't know where to start" → [README.md](./README.md)
- "Which phase?" → Phase Selection table above
- "How do I execute?" → Task type tables above
- "Need to set up?" → [SETUP.md](./SETUP.md)
- "What's the structure?" → [STRUCTURE.txt](./STRUCTURE.txt)

---

## 📝 Update History

These instructions are living documents. They may be updated as team practices evolve. Always check for the latest version in your repository.

| Date       | Version | Description     | Author | Status           |
| ---------- | ------- | --------------- | ------ | ---------------- |
| 2026-09-20 | 1.0.0   | Initial version | vduczz | Production Ready |

> For the latest updates, check your repository's `.agent-instructions/` directory.
