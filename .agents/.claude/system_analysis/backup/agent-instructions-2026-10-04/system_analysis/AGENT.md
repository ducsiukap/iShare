# System Analysis Phase - Agent Rules & Procedures

This phase focuses on understanding systems, defining requirements, and designing architecture before implementation begins.

---

## 🎯 Phase Overview

**Goal:** Create clear specifications and design decisions that guide design and coding phases.

**When to use this phase:**
- Interviewing stakeholders to gather product requirements (Business Analysis)
- Analyzing existing systems
- Defining requirements and specifications
- Designing database schemas
- Planning APIs and contracts
- Performance analysis
- Creating architectural decisions

**Typical workflow:** Interview → Analyze → Design → Document → Approve

**Deliverables:** System specifications, diagrams, requirements documentation, data models, ADRs, interview registers

---

## 📋 Mandatory Rules

### Phase-Specific Rules
Read the **4 Mandatory Rules for System Analysis** in detail:
→ [SYSTEM_ANALYSIS_RULES.md](./SYSTEM_ANALYSIS_RULES.md)

**Quick summary:**
1. **Think Big Picture First** — Understand entire system context before details
2. **Document Everything Clearly** — Every decision, diagram, spec needs explanation
3. **Understand Relationships & Dependencies** — Map component relationships and data flows
4. **Validate Assumptions with Stakeholders** — Never assume, always confirm with real users

### Interview Protocol (When doing BA work)
If your task involves conducting stakeholder interviews to gather requirements, follow the complete **Business Analysis Interview Rules**:
→ [BA-INTERVIEW-RULES.md](./BA-INTERVIEW-RULES.md)

**Quick summary:**
- Never invent requirements
- Every requirement must be traceable (DRAFT § or QA-###)
- Complete 9-phase structured interview (Phase 0-9)
- Maintain 5 live registers (Issue Queue, QA Log, Open Issues, Assumptions, Decisions)
- No spec writing until interview is complete
- Requirements are behavior, not design
- All output in English, all files in `iShare/docs/_temp/`
- **Exception (DEC-139):** System Requirement documents are written in Vietnamese, per module, under `.agents/.claude/system_analysis/output/specs/` — see [SR-DOCUMENT-RULES.md](./SR-DOCUMENT-RULES.md)

---

## 6 Task Types with Procedures

### Task Type 1: System Architecture Analysis

**Purpose:** Analyze existing or planned system structure and identify improvements.

**Inputs Required:**
- Current system diagram or description
- Performance metrics (if existing system)
- Business goals and constraints
- Growth projections

**Output Specifications:**
- Architecture diagram (visual with labels)
- Module/component inventory
- Data flow diagram
- Technology recommendations
- Identified bottlenecks
- Improvement recommendations

**Procedure:**

1. **Understand Current State**
   - Gather existing documentation
   - Interview current users/developers
   - Document current architecture
   - Identify pain points

2. **Analyze**
   - Map all components
   - Identify data flows
   - Document integrations
   - Highlight bottlenecks
   - List technical debt

3. **Design Future State**
   - Propose architecture options (2-3 options)
   - For each option: pros, cons, time estimate
   - Select recommended approach with justification

4. **Document**
   - Create clear architecture diagram
   - Write narrative explanation
   - Include technology stack recommendations
   - Document migration path (if changing existing)

5. **Validate**
   - Review with stakeholders
   - Address concerns
   - Get approval to proceed

**Recommended Tools:**
- Mermaid or PlantUML for diagrams
- Figma for visual architecture
- OpenAPI/Swagger for API design

**Output Location:** `iShare/docs/_temp/architecture/`

**Pre-Delivery Checklist:**
- [ ] Architecture diagram is clear and complete
- [ ] All components are labeled and explained
- [ ] Data flows are documented
- [ ] Technology choices justified
- [ ] Scalability considerations addressed
- [ ] Security considerations addressed
- [ ] Integration points identified
- [ ] Migration plan documented (if applicable)
- [ ] Alternatives considered and compared
- [ ] Stakeholder approval obtained

**Time estimate:** 4-6 hours

---

### Task Type 2: Requirements & Use Cases (BA-Driven)

**Purpose:** Define what the system needs to do and how users will interact with it through structured stakeholder interviews.

**Note:** This is the primary Business Analysis task. Follow the complete **9-phase interview protocol** in [BA-INTERVIEW-RULES.md](./BA-INTERVIEW-RULES.md).

**Inputs Required:**
- Product draft and summary (from stakeholder)
- Business goals and objectives
- User profiles/personas
- Stakeholder availability for interview

**Output Specifications:**
- Complete interview registers (QA Log, Issue Queue, Assumptions, Decisions)
- SPEC-000-index.md (product overview, module map, feature index)
- SPEC-001-glossary.md (all terms and acronyms)
- SPEC-002-actors-and-permissions.md (actors, roles, permission matrix)
- SPEC-003-data-model.md (entities, attributes, relationships)
- SPEC-004-nfr.md (non-functional requirements)
- SPEC-005-open-issues.md (open issues, assumptions, decisions)
- SPEC-<MOD>-<NN>-<feature-slug>.md (one file per feature)

**Procedure:**

Follow all **9 phases** from [BA-INTERVIEW-RULES.md](./BA-INTERVIEW-RULES.md):

- **Phase 0:** Intake & gap analysis
- **Phase 1:** Business context
- **Phase 2:** Actors, roles & permissions
- **Phase 3:** Scope decomposition (module level)
- **Phase 4:** Feature decomposition (per module)
- **Phase 5:** Feature deep dive (main work)
- **Phase 6:** Cross-cutting concerns
- **Phase 7:** Non-functional requirements
- **Phase 8:** Data model & integrations
- **Phase 9:** Open issue clearing round

**For each phase:**
1. Create Issue Queue (ISS-###) with all unclear points
2. Ask one issue per message (Blocker → Major → Minor)
3. Record answer as QA-###
4. Close issue and move to next
5. Playback scope summary for confirmation before next phase

**Output Location:** `iShare/docs/_temp/specs/` — one file per feature

**Key Deliverables:**
- Every FR has traceable source (DRAFT § or QA-###)
- Every FR is atomic and testable (no vague words)
- Every assumption documented (ASM-###) and confirmed
- Every open issue tracked (OPEN-###)
- Complete glossary of domain terms
- Permission matrix reviewed and approved
- All specification files in English

**Pre-Delivery Checklist:**
- [ ] All 9 interview phases completed
- [ ] Every requirement has traceable source (DRAFT § or QA-###)
- [ ] No vague words (fast, easy, user-friendly, etc.)
- [ ] All requirements are atomic and testable
- [ ] User personas documented
- [ ] User stories clear with acceptance criteria
- [ ] Use cases cover happy path and exceptions
- [ ] User flows easy to follow
- [ ] Priorities assigned (must-have, should-have, nice-to-have)
- [ ] Stakeholder feedback incorporated
- [ ] No conflicting requirements
- [ ] All acronyms in glossary
- [ ] Approval documented
- [ ] Every file valid Markdown, in English
- [ ] All files stored in `iShare/docs/_temp/specs/`

**Time estimate:** 8-16 hours (depends on product complexity)

---

### Task Type 3: Database Schema Design

**Purpose:** Design the database structure to efficiently store and retrieve data based on validated requirements.

**Inputs Required:**
- Requirements from BA phase (what data needs to be stored)
- Data volume and growth projections
- Access patterns (how will data be queried?)
- Performance requirements

**Output Specifications:**
- Entity-Relationship (ER) diagram
- Database schema (DDL script)
- Index strategy
- Data migration plan (if applicable)
- Performance considerations

**Procedure:**

1. **Identify Entities**
   - What data needs to be stored?
   - What are the main entities?
   - What attributes does each have?

2. **Define Relationships**
   - How do entities relate? (1:1, 1:N, M:N)
   - What are the foreign keys?
   - Are there constraints?

3. **Normalize Schema**
   - Apply normal forms (typically 3NF)
   - Identify and resolve redundancies
   - Check for anomalies

4. **Design for Performance**
   - Identify common queries
   - Plan indexes
   - Consider denormalization (if needed)
   - Plan for data volume

5. **Document**
   - Create ER diagram
   - Write DDL script (CREATE TABLE statements)
   - Document indexes and keys
   - Explain design decisions

6. **Validate**
   - Review with database expert
   - Test with realistic data volumes
   - Get approval

**Output Location:** `iShare/docs/_temp/data-model/`

**Recommended Tools:**
- Mermaid for ER diagrams
- SQL for DDL script

**Pre-Delivery Checklist:**
- [ ] ER diagram is clear and complete
- [ ] All entities and relationships documented
- [ ] Primary and foreign keys defined
- [ ] Data types appropriate
- [ ] Indexes planned for common queries
- [ ] Scalability considered
- [ ] Constraints documented
- [ ] No data redundancy issues
- [ ] Migration plan addressed (if applicable)
- [ ] Performance review completed

**Time estimate:** 3-4 hours

---

### Task Type 4: API Contract Design

**Purpose:** Define the API specification that other systems will use to interact with this system.

**Inputs Required:**
- System requirements from BA phase
- Client requirements (mobile, web, etc.)
- Performance requirements
- Authentication/authorization needs

**Output Specifications:**
- OpenAPI/Swagger specification
- Request/response examples
- Error handling documentation
- Authentication flow
- Rate limiting policy
- API documentation

**Procedure:**

1. **Define Endpoints**
   - What operations does the API support?
   - For each operation: HTTP method, path, parameters

2. **Define Request/Response Formats**
   - What data is sent in requests?
   - What data is returned in responses?
   - What are valid values/ranges?

3. **Plan Error Handling**
   - What errors can occur?
   - What HTTP status codes?
   - What error messages?

4. **Define Security**
   - How is authentication handled?
   - How are permissions checked?
   - Are there rate limits?

5. **Create OpenAPI Spec**
   - Document all endpoints
   - Include request/response examples
   - Document error responses
   - Document authentication

6. **Validate**
   - Review with API consumers
   - Test specification with examples
   - Get approval

**Output Location:** `iShare/docs/_temp/api/`

**Recommended Tools:**
- Swagger Editor for OpenAPI specs
- Postman for testing

**Pre-Delivery Checklist:**
- [ ] OpenAPI specification complete
- [ ] All endpoints documented
- [ ] Request/response examples provided
- [ ] Error handling documented
- [ ] Authentication flow explained
- [ ] Rate limiting policy defined
- [ ] Data types consistent
- [ ] Backward compatibility considered
- [ ] Security review completed
- [ ] Client feedback incorporated

**Time estimate:** 2-3 hours

---

### Task Type 5: Architecture Decision Record (ADR)

**Purpose:** Document important architectural decisions and their trade-offs discovered during analysis.

**Inputs Required:**
- Decision to be made
- Context and constraints
- Possible alternatives
- Stakeholder feedback

**Output Specifications:**
- ADR document with: decision, context, consequences, alternatives
- Diagram showing impact (if applicable)
- Implementation guidance

**Procedure:**

1. **State the Decision**
   - What decision needs to be made?
   - Why is it important?
   - Who needs to agree?

2. **Document Context**
   - What problem led to this decision?
   - What constraints exist?
   - What assumptions are we making?

3. **List Alternatives**
   - What options did we consider?
   - For each: pros, cons, time/cost estimate

4. **Make the Decision**
   - Which alternative do we choose?
   - Why is this the best choice?
   - What trade-offs are we accepting?

5. **Document Consequences**
   - What are the immediate impacts?
   - What are long-term implications?
   - What risks do we accept?

6. **Plan Implementation**
   - How will we implement this decision?
   - What needs to change?
   - How will we validate it worked?

**Example ADR:**
```markdown
# ADR-001: Microservices vs. Monolith

## Status: Accepted

## Context
Current monolithic system is becoming hard to scale independently.
Need decision on future architecture.
Constraints: 3-month timeline, existing team of 8

## Decision
Adopt modular monolith as intermediate step, migrate to microservices later.

## Rationale
- Less disruption than immediate microservices migration
- Allows independent scaling of modules over time
- Team can learn microservices patterns gradually
- Keeps timeline realistic

## Alternatives Considered
1. Stay with monolith → Scaling issues remain
2. Full microservices immediately → Too risky, too long
3. Modular monolith (chosen) → Balanced approach

## Consequences
- Positive: Reduced risk, faster migration
- Negative: Not full microservices benefits initially
- Risk: Migration to microservices might be complex

## Implementation Plan
[Details on how to implement]
```

**Output Location:** `iShare/docs/_temp/adr/`

**Recommended Tools:**
- Markdown for ADR document
- Mermaid for diagrams showing impact

**Pre-Delivery Checklist:**
- [ ] Decision clearly stated
- [ ] Context and constraints documented
- [ ] All alternatives explored and compared
- [ ] Rationale for chosen approach explained
- [ ] Consequences clearly stated (positive and negative)
- [ ] Risks and trade-offs acknowledged
- [ ] Implementation plan outlined
- [ ] Stakeholder agreement obtained
- [ ] Related ADRs referenced
- [ ] Document is versioned and archived

**Time estimate:** 2-3 hours

---

### Task Type 6: Performance & Scalability Analysis

**Purpose:** Analyze current/projected performance and identify optimization opportunities based on requirements.

**Inputs Required:**
- Current system performance metrics (if existing)
- User growth projections from requirements phase
- SLA/performance requirements from NFR phase
- Expected usage patterns

**Output Specifications:**
- Current performance baseline
- Bottleneck analysis
- Scalability recommendations
- Performance optimization plan
- Monitoring strategy
- Capacity planning

**Procedure:**

1. **Establish Baseline**
   - Measure current performance (if existing system)
   - Document: response times, throughput, resource usage
   - Identify current bottlenecks

2. **Project Future Needs**
   - User growth: How many users in 1, 2, 5 years?
   - Load patterns: Peak vs. average
   - Data volume: How much data growth?

3. **Identify Bottlenecks**
   - Database queries: Which are slow?
   - Application code: What's inefficient?
   - Infrastructure: CPU, memory, network limits
   - External dependencies: Third-party APIs

4. **Analyze Scalability**
   - Horizontal scaling: Add more servers
   - Vertical scaling: Bigger servers
   - Database scaling: Sharding, replication
   - Caching strategies

5. **Recommend Optimizations**
   - Quick wins: Low effort, high impact
   - Medium term: Moderate effort, good impact
   - Long term: Complex changes, major impact

6. **Plan Monitoring**
   - What metrics to track?
   - Alert thresholds?
   - Dashboards?

**Output Location:** `iShare/docs/_temp/performance/`

**Recommended Tools:**
- Performance monitoring tools
- Load testing tools
- Capacity planning spreadsheets
- Mermaid for architecture diagrams

**Pre-Delivery Checklist:**
- [ ] Current baseline documented
- [ ] Growth projections realistic
- [ ] Bottleneck analysis complete
- [ ] Scalability options evaluated
- [ ] Performance targets defined
- [ ] Optimization priorities ranked
- [ ] Implementation effort estimated
- [ ] Costs (if applicable) documented
- [ ] Monitoring strategy defined
- [ ] Assumptions documented

**Time estimate:** 4-6 hours

---

## Recommended Tools

### For Interviews & Tracking:
- **Spreadsheets** (Google Sheets, Excel) — Issue Queue, QA Log, Assumption Register, Glossary
- **Markdown** (.md) — Interview notes, register excerpts

### For Diagrams:
- **Mermaid** (free, code-based) — ER diagrams, flowcharts, architecture, use case diagrams
- **PlantUML** (free, code-based) — Detailed diagrams
- **Figma** (free/paid) — Visual architecture, system diagrams, user flows
- **Draw.io** (free) — General purpose diagramming

### For Specifications:
- **Markdown** (.md) — All specification files
- **OpenAPI/Swagger** — API specifications

### For Collaboration:
- **Google Docs** — Real-time editing with stakeholders
- **Slack/Discord** — Team discussion

---

## Quick Reference: When to Use System Analysis

| Trigger | Task Type | Time |
|---------|-----------|------|
| "Interview stakeholders for requirements" | Requirements & Use Cases (BA) | 8-16h |
| "Redesign our system" | Architecture Analysis | 4-6h |
| "Design the database" | Database Schema | 3-4h |
| "Define the API" | API Contract | 2-3h |
| "Document our choice" | Architecture Decision | 2-3h |
| "Optimize performance" | Performance Analysis | 4-6h |

---

## File Storage Structure

All temporary work and outputs go to `iShare/docs/_temp/`:

```
iShare/docs/_temp/
├── specs/                          # Specification files
│   ├── SPEC-000-index.md
│   ├── SPEC-001-glossary.md
│   ├── SPEC-002-actors-and-permissions.md
│   ├── SPEC-003-data-model.md
│   ├── SPEC-004-nfr.md
│   ├── SPEC-005-open-issues.md
│   └── SPEC-<MOD>-<NN>-<feature-slug>.md
├── architecture/                   # Architecture files
│   └── architecture.md
├── data-model/                     # Database design files
│   └── schema.md
├── api/                            # API specification files
│   └── openapi.yaml
├── adr/                            # Architecture Decision Records
│   └── adr-001-*.md
├── performance/                    # Performance analysis files
│   └── performance-analysis.md
└── registers/                      # Interview tracking (optional)
    ├── qa-log.md
    ├── issue-queue.md
    ├── assumptions-register.md
    ├── decisions-log.md
    └── glossary.md
```

---

## Phase Navigation

**What's next after System Analysis?**
- If approved → Move to [Design Phase](../design/AGENT.md)
- If needs revision → Refine analysis, re-validate with stakeholders
- If approved for specific features only → Design features one at a time

**Before you start:** Read [COMMON-RULES.md](../COMMON-RULES.md)

**Questions?** Check [README.md](../README.md) or [NAVIGATION.md](../NAVIGATION.md)

**Detailed rules:**
- [SYSTEM_ANALYSIS_RULES.md](./SYSTEM_ANALYSIS_RULES.md) — 4 mandatory rules
- [BA-INTERVIEW-RULES.md](./BA-INTERVIEW-RULES.md) — Complete BA interview protocol (9 phases, registers, spec template)
