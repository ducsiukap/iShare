---
name: technical-design
description: System design tasks for iShare outside the interview — architecture analysis, database schema, API contract, architecture decision records, performance analysis. Use for Phase 7 (NFR) and Phase 8 (data model) work and any technical design question.
---

# Role: Technical Design

> Phase: **System Analysis** → [../../phases/system-analysis.md](../../phases/system-analysis.md) · Inputs come from the registers and FR documents produced with [ba-interview](../ba-interview/SKILL.md) and [analyzing-functional-requirements](../analyzing-functional-requirements/SKILL.md). Common rules: [../../COMMON-RULES.md](../../COMMON-RULES.md)

**Output location (all tasks):** `.agents/.claude/system_analysis/output/<folder>/` — `architecture/`, `data-model/`, `api/`, `adr/`, `performance/`. Final versions are promoted to `docs/approved/` after stakeholder approval.

**iShare note (Phase 8):** the stakeholder expects the data model to be derived module by module — extract nouns → entities and attributes → system-wide entity diagram → database → class and flow design. The inputs for this work are the FR documents (`FR-Mxx.md`): section 5 business rules, business data with the CRUD matrix, state transitions and interfaces with other modules. Database and model design is not a requirement and does not belong in an FR document.

| Trigger | Task | Time |
|---|---|---|
| "Redesign our system" | 1. Architecture Analysis | 4-6h |
| "Design the database" | 2. Database Schema | 3-4h |
| "Define the API" | 3. API Contract | 2-3h |
| "Document our choice" | 4. Architecture Decision Record | 2-3h |
| "Optimize performance" | 5. Performance Analysis | 4-6h |

---

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

**Output Location:** `.agents/.claude/system_analysis/output/architecture/`

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

---

### Task Type 2: Database Schema Design

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

**Output Location:** `.agents/.claude/system_analysis/output/data-model/`

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

---

### Task Type 3: API Contract Design

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

**Output Location:** `.agents/.claude/system_analysis/output/api/`

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

---

### Task Type 4: Architecture Decision Record (ADR)

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

**Output Location:** `.agents/.claude/system_analysis/output/adr/`

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

---

### Task Type 5: Performance & Scalability Analysis

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

**Output Location:** `.agents/.claude/system_analysis/output/performance/`

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

---

## Recommended Tools

### For Diagrams:
- **Mermaid** (free, code-based) — ER diagrams, flowcharts, architecture
- **PlantUML** (free, code-based) — detailed diagrams
- **Draw.io** / **Figma** — visual architecture and system diagrams

### For Specifications:
- **Markdown** (.md) — all specification files
- **OpenAPI/Swagger** — API specifications
