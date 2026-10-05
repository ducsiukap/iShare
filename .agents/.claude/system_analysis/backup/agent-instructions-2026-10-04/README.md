# Agent Instructions

Welcome to the Agent Instructions documentation. This directory contains comprehensive guidelines for agents working across three distinct phases of software development.

---

## 🚀 Quick Start (30 seconds)

1. **Create your workspace** → [WORKSPACE-SETUP.md](./WORKSPACE-SETUP.md) (first time only)
2. **Read the common rules** → [COMMON-RULES.md](./COMMON-RULES.md)
3. **Identify your phase** → Which one describes your task?
   - 🔍 **System Analysis** - Understanding requirements, designing architecture
   - 🎨 **Design** - Creating mockups, user flows, design systems
   - 💻 **Coding** - Writing code, fixing bugs, testing, deployment
4. **Read the rules** → Go to `.agent-instructions/[phase]/AGENT.md`
5. **Execute the task** → Follow the phase-specific procedures

---

## 🎯 Phase Selection Flowchart

```
START
  ↓
Does your task involve writing/fixing/testing code?
  ├─ YES → Go to CODING phase
  ├─ NO  ↓
  │    Does your task involve creating visual designs/mockups?
  │      ├─ YES → Go to DESIGN phase
  │      ├─ NO  ↓
  │    Are you analyzing systems, defining requirements, architecture?
  │      └─ YES → Go to SYSTEM_ANALYSIS phase
  │
  └─ NOT SURE? Read COMMON-RULES.md first
```

---

## 📚 Quick Links by Phase

| Phase              | File                                                   | Best For                                                   |
| ------------------ | ------------------------------------------------------ | ---------------------------------------------------------- |
| 🔍 System Analysis | [system_analysis/AGENT.md](./system_analysis/AGENT.md) | Architecture, requirements, database design, API contracts |
| 🎨 Design          | [design/AGENT.md](./design/AGENT.md)                   | UI mockups, user flows, design systems, prototypes         |
| 💻 Coding          | [coding/AGENT.md](./coding/AGENT.md)                   | Features, bug fixes, tests, refactoring, deployments       |

---

## 🏗️ The Three Phases - Overview

### Phase 1: 🔍 System Analysis

**Goal:** Understand requirements, design systems, plan architecture

**When to use:**

- Analyzing existing systems
- Defining requirements and specifications
- Designing database schemas
- Planning APIs and contracts
- Performance analysis
- Creating architectural decisions

**Deliverables:** Architecture diagrams, specifications, requirements documents, database schemas, API contracts, ADRs

**Phase file:** [system_analysis/AGENT.md](./system_analysis/AGENT.md)

---

### Phase 2: 🎨 Design

**Goal:** Create visual designs, user experiences, and component systems

**When to use:**

- Creating UI mockups and wireframes
- Designing user flows and interactions
- Building design systems
- Creating prototypes
- Designing for responsive layouts
- Conducting design reviews

**Deliverables:** Wireframes, mockups, user flow diagrams, design systems, prototypes, design specifications

**Phase file:** [design/AGENT.md](./design/AGENT.md)

---

### Phase 3: 💻 Coding

**Goal:** Implement features, fix bugs, test, and deploy

**When to use:**

- Writing new features
- Fixing bugs
- Refactoring code
- Writing tests
- Optimizing performance
- Deploying to production

**Deliverables:** Source code, test suites, documentation, git commits, pull requests

**Phase file:** [coding/AGENT.md](./coding/AGENT.md)

---

## 🔄 Workflow Diagram

```
Task Received
    ↓
[IDENTIFY PHASE]
├─ System Analysis? → Read rules → Execute SA tasks
├─ Design? → Read rules → Execute Design tasks
└─ Coding? → Read rules → Execute Coding tasks
    ↓
[FOLLOW PHASE RULES]
├─ Mandatory Rules (4-5 rules per phase)
├─ Task-specific procedures
└─ Pre-delivery checklists
    ↓
[EXECUTE TASK]
├─ Create temp work in .agents/.[agent-name]/[phase]/
├─ Follow step-by-step procedures
└─ Maintain quality standards
    ↓
[DELIVER]
├─ Pass QA checklist
├─ Output in .md format (when possible)
├─ Communicate in English (default)
└─ Deliver to user (not in .agents/)
```

---

## 📋 Universal Rules Apply to All Phases

Before reading phase-specific rules, ensure you understand the **10 Common Rules** that apply everywhere:

1. **Output Language:** English is default
2. **Output Format:** Markdown (.md) when possible
3. **Temporary Storage:** `.agents/.[agent-name]/[phase]/`
4. **Confirmation Workflow:** Ask before direct edits (unless told to "edit")
5. **Format by Phase:** Different standards for each phase
6. **Code Standards:** Quality, tests, documentation
7. **Documentation:** Purpose, context, usage, examples
8. **QA Before Delivery:** Pre-delivery checklist required
9. **Git Workflow:** Clear English commit messages
10. **Communication:** Clear, structured, with checkpoints

**See:** [COMMON-RULES.md](./COMMON-RULES.md)

---

## 🚀 Quick Start (5 Steps)

1. **Set up your workspace** (first time only)
   - [WORKSPACE-SETUP.md](./WORKSPACE-SETUP.md) - Create your `.agents/.[agent-name]/` temporary directory

2. **Identify your phase**
   - What type of work are you doing? SA, Design, or Coding?

3. **Read the common rules**
   - [COMMON-RULES.md](./COMMON-RULES.md) (applies to everything)

4. **Read phase-specific rules**
   - [system_analysis/AGENT.md](./system_analysis/AGENT.md)
   - [design/AGENT.md](./design/AGENT.md)
   - [coding/AGENT.md](./coding/AGENT.md)

5. **Execute following checklists**
   - Use pre-delivery checklists before finishing
   - Output in English, .md format
   - Save temporary work in `.agents/.[agent-name]/`

---

## 📁 Directory Structure

```
.agent-instructions/
├── README.md                      # Entry point (you are here)
├── COMMON-RULES.md                # 10 universal rules for all agents
├── NAVIGATION.md                  # How to find what you need
├── ARCHITECTURE.md                # Directory structure & concepts
├── WORKSPACE-SETUP.md             # Agent workspace setup guide
└── [phases]/
    ├── system_analysis/AGENT.md
    ├── design/AGENT.md
    └── coding/AGENT.md

.agents/
└── .[agent-name]/                 # Your agent workspace (e.g., .claude, .gpt)
    ├── system_analysis/           # SA phase drafts
    ├── design/                    # Design phase drafts
    └── coding/                    # Coding phase drafts
```

---

## 🔗 Navigation by Need

**Need to set up your workspace?**  
→ Follow [WORKSPACE-SETUP.md](./WORKSPACE-SETUP.md) to create `.agents/.[agent-name]/`

**Need detailed guidance on a task?**  
→ Check [NAVIGATION.md](./NAVIGATION.md) for comprehensive index

**Want to understand the structure?**  
→ See [ARCHITECTURE.md](./ARCHITECTURE.md) for directory organization

**Ready to execute right now?**  
→ Go directly to your phase's AGENT.md file above

---

## 📚 Learning Paths

### 5-Day Onboarding

**Day 1: Setup & Foundations**

- Set up your workspace: [WORKSPACE-SETUP.md](./WORKSPACE-SETUP.md)
- Read [README.md](./README.md) (this file)
- Read [COMMON-RULES.md](./COMMON-RULES.md)

**Day 2: Understanding Phases**

- Understand the 3 phases and when to use each
- Review phase descriptions above

**Day 3: Deep Dive**

- Read your primary phase's AGENT.md file
- Understand the mandatory rules for your phase
- Review task types in your phase

**Day 4: Procedures**

- Study the step-by-step procedures for your phase
- Review pre-delivery checklists
- Understand common mistakes to avoid

**Day 5: Practice**

- Execute your first task
- Follow checklists religiously
- Get feedback from team

---

## ✅ Pre-Execution Checklist

Before starting any task:

- [ ] I've set up my workspace: [WORKSPACE-SETUP.md](./WORKSPACE-SETUP.md)
- [ ] I've read this README.md
- [ ] I've read [COMMON-RULES.md](./COMMON-RULES.md)
- [ ] I've read the phase-specific AGENT.md file
- [ ] I understand the mandatory rules for my phase
- [ ] I know which task type I'm executing
- [ ] I have the pre-delivery checklist for my task type
- [ ] I have the `.agents/.[agent-name]/` directory structure ready
- [ ] I understand when to ask for confirmation vs. direct edits

---

## 🎯 Key Concepts

**Phase Identification:** Determines which rules apply  
**Task Type:** Determines procedures and checklists  
**Mandatory Rules:** Non-negotiable requirements per phase  
**Pre-delivery Checklist:** Quality gate before finishing  
**Temporary Directory:** `.agents/.[agent-name]/[phase]/` for drafts  
**Output Format:** English, Markdown, delivered to user (not in .agents/)  
**Workspace Setup:** Create once, reuse for all tasks

---

## 🔧 Common Questions

**Q: How do I set up my workspace?**  
A: Read [WORKSPACE-SETUP.md](./WORKSPACE-SETUP.md) - it takes 2 minutes

**Q: What if my task spans multiple phases?**  
A: Read [NAVIGATION.md](./NAVIGATION.md) section on "Multi-phase Tasks"

**Q: When should I ask for confirmation?**  
A: Read [COMMON-RULES.md](./COMMON-RULES.md) Rule 4 in detail

**Q: How do I organize temporary work?**  
A: Follow `.agents/.[agent-name]/[phase]/` structure, see [WORKSPACE-SETUP.md](./WORKSPACE-SETUP.md)

**Q: What format should I use for output?**  
A: Markdown (.md) when possible, phase-specific format when required

**Q: Do I commit .agents/ directory to git?**  
A: No! Add `.agents/` to `.gitignore`, see [WORKSPACE-SETUP.md](./WORKSPACE-SETUP.md)

---

## 📞 Support

**Need to set up workspace?** → [WORKSPACE-SETUP.md](./WORKSPACE-SETUP.md)  
**Need to find something?** → [NAVIGATION.md](./NAVIGATION.md)  
**Need common rules?** → [COMMON-RULES.md](./COMMON-RULES.md)  
**Phase-specific help?** → See your phase's AGENT.md above

---

## 📝 Update History

These instructions are living documents. They may be updated as team practices evolve. Always check for the latest version in your repository.

| Date       | Version | Description     | Author | Status           |
| ---------- | ------- | --------------- | ------ | ---------------- |
| 2026-09-20 | 1.0.0   | Initial version | vduczz | Production Ready |
