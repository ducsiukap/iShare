# Common Rules for All Agents

These 10 rules apply to **every agent, every phase, every task**. Read and follow them without exception.

---

## Rule 1: Output Language - English is Default

**The Rule:**
- **Default output language:** ENGLISH
- If the task specifies a different language requirement, use that language
- Always document language decisions in comments/headers
- When translating content, include both source and target

**Why it matters:**
- Ensures consistency across all documentation
- Makes knowledge searchable and shareable
- Maintains professional standards for team collaboration

**Examples:**

✅ **Correct:**
```
User says: "Create API documentation"
→ Output: English documentation (.md format)
```

✅ **Correct:**
```
User says: "Viết tài liệu tiếng Việt cho feature này"
→ Output: Vietnamese documentation (explicitly requested)
→ Note: Include language marker: "[Vietnamese Doc]"
```

❌ **Wrong:**
```
User says: "Create API documentation"
→ Output: Random mix of English and Vietnamese
```

---

## Rule 2: Output Format - Markdown is Preferred

**The Rule:**
- **Default output format:** Markdown (.md)
- Use `.md` for all text documentation, specifications, guides
- Structure content with clear headings, sections, and examples
- Use code blocks with language specifiers for code examples
- Use tables for structured data

**Markdown Structure Guidelines:**
```markdown
# Main Heading (H1)
Brief overview paragraph

## Section Heading (H2)
Content with context

### Subsection (H3)
Detailed information

**Bold for emphasis**
`code for inline code`

```
Multi-line code blocks with language
```

- Bullet lists for items
- [ ] Checklists for tasks
- | Tables | for | data |
```

**When to use alternatives:**
- Use YAML for configuration files
- Use JSON for data/API responses
- Use HTML/SVG for diagrams (export from Figma/Mermaid)
- Use plain text (.txt) only for special cases (file trees, raw logs)

**Examples:**

✅ **Correct:**
```
Task: "Document the API endpoints"
→ Output: OpenAPI/Swagger spec as .md with examples
→ Include tables, code blocks, sections
```

✅ **Correct:**
```
Task: "Create configuration"
→ Output: config.yaml (YAML format is appropriate here)
```

❌ **Wrong:**
```
Task: "Document the API"
→ Output: Microsoft Word .docx file
→ Reason: Not version-control friendly, not searchable
```

---

## Rule 3: Temporary Work Storage

**The Rule:**
- All temporary/draft work goes into: `.agents/.[agent-name]/[phase]/`
- Example paths:
  - `.agents/.claude/system_analysis/` - SA phase drafts
  - `.agents/.claude/design/` - Design phase drafts
  - `.agents/.claude/coding/` - Coding phase drafts
- Temporary work includes: drafts, research, experiments, intermediate outputs
- Final deliverables are delivered to the user (not left in `.agents/`)

**Directory Structure:**
```
.agents/
└── .claude/                    # Agent workspace
    ├── system_analysis/        # SA phase work
    │   ├── research.md
    │   ├── draft_architecture.md
    │   └── diagrams/
    ├── design/                 # Design phase work
    │   ├── wireframes_draft.md
    │   ├── user_flows.md
    │   └── assets/
    └── coding/                 # Coding phase work
        ├── implementation_plan.md
        ├── test_cases.md
        └── code_snippets/
```

**Why this matters:**
- Keeps project root clean
- Makes it easy to differentiate between drafts and final work
- Provides a workspace for experiments without affecting production
- `.agents/` should be added to `.gitignore`

**Git Configuration:**
```bash
# Add to .gitignore
echo ".agents/" >> .gitignore
```

**Examples:**

✅ **Correct:**
```
Agent is researching architecture
→ Save draft to: .agents/.claude/system_analysis/research.md
→ Review with user
→ Deliver final version to user (not in .agents/)
```

✅ **Correct:**
```
Agent is creating wireframes
→ Save drafts to: .agents/.claude/design/wireframes_v1.md
→ Iterate: wireframes_v2.md, wireframes_v3.md
→ Export final to user
```

❌ **Wrong:**
```
Agent saves all work directly to project root
→ Creates clutter, mixes drafts with final work
```

---

## Rule 4: Output Confirmation & Direct Editing Workflow

**The Rule:**
- **NEVER edit files directly** unless the task explicitly says "edit", "modify", "fix", "update", or equivalent
- **ALWAYS ask for confirmation** before direct edits
- If task has direct edit instruction → Skip confirmation, proceed directly
- If task does NOT have direct edit instruction → Ask which approach:
  - Create commented/annotated version in temporary directory?
  - Edit the file directly?

**Task Keywords Meaning "Direct Edit":**
- English: "edit", "fix", "modify", "update", "refactor", "change", "improve", "correct", "implement"
- Vietnamese: "sửa", "sửa trực tiếp", "cập nhật", "thay đổi", "cải thiện", "chữa lỗi"

**Workflow Diagram:**
```
User gives task
    ↓
Does task say "edit/modify/fix/update" (EN) or "sửa/cập nhật" (VN)?
    ├─ YES  → Direct Edit Path
    │         ├─ Proceed directly (no confirmation needed)
    │         ├─ Make edits to production files
    │         └─ Deliver with changelog
    │
    └─ NO   → Confirmation Path
              ├─ Create commented version in .agents/.claude/[phase]/
              ├─ Ask user: "Should I edit directly or deliver as draft?"
              ├─ Wait for response
              └─ Proceed based on user choice
```

**Scenario Examples:**

**Scenario 1: Direct Edit Instruction Present**
```
User: "Fix the bug in the login controller where username validation fails"

Analysis:
- Task contains "Fix" → Direct edit instruction
- Action: Proceed directly without asking
- Step 1: Identify the bug in the code
- Step 2: Create fix
- Step 3: Test the fix
- Step 4: Deliver the fixed file with changelog
```

**Scenario 2: No Direct Edit Instruction**
```
User: "I created this API specification but I think there are some issues"

Analysis:
- Task does NOT contain edit instruction
- No explicit "fix", "modify", "update", etc.
- Action: Ask for confirmation

My response:
"I've reviewed the API specification and found 3 issues:
1. [issue description]
2. [issue description]
3. [issue description]

Should I:
A) Create a corrected version in .agents/.claude/system_analysis/api_spec_v2.md
   (as a draft for your review)?
B) Edit your original file directly?"
```

**Scenario 3: Ambiguous Task**
```
User: "Can you help with this design file?"

Analysis:
- Task does NOT clearly indicate direct editing
- Action: Ask for clarification

My response:
"I'd be happy to help! Could you clarify:
- Should I create suggestions/feedback as a separate document?
- Or would you like me to edit your file directly?"
```

**When to Create Temporary Versions:**
- Task requires feedback/review before final edits
- Multiple iterations likely needed
- Client wants to approve changes first
- Safety: Preserve original file until approval

**When to Edit Directly:**
- Task explicitly says "edit", "fix", "modify", "update"
- Client has pre-approved the approach
- Bug fix or urgent correction needed
- Refactoring with clear scope

---

## Rule 5: Output Format by Phase

**System Analysis Phase:**
- Primary format: Markdown (.md)
- Diagrams: Mermaid, PlantUML (export as SVG/PNG)
- Specifications: OpenAPI/Swagger YAML
- Data: Use tables and structured lists

**Design Phase:**
- Primary format: Figma design files (exported as .md for documentation)
- Wireframes: SVG, PNG, or Figma components
- User flows: Mermaid diagrams, flowcharts
- Design systems: Component documentation in .md

**Coding Phase:**
- Primary format: Source code (JavaScript, Python, etc.)
- Tests: Jest, Mocha, or language-specific test framework
- Documentation: Markdown (.md) for guides, comments in code
- Git commits: Clear, descriptive English messages

---

## Rule 6: Code Output Standards

**When delivering code:**
- Always include unit tests (minimum 80% coverage)
- Add inline comments for complex logic
- Follow the project's code style and conventions
- Include error handling and edge cases
- Document functions/methods with JSDoc or equivalent
- Use English variable names and comments

**Example:**
```javascript
/**
 * Validates user email format
 * @param {string} email - The email to validate
 * @returns {boolean} True if email is valid
 * @throws {Error} If email is empty
 */
function validateEmail(email) {
  if (!email) throw new Error('Email cannot be empty');
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}
```

---

## Rule 7: Documentation Requirements

**For every deliverable:**
1. **Purpose statement** - What does it do?
2. **Context** - Why was it created?
3. **Usage** - How to use/implement it?
4. **Examples** - Real-world examples
5. **Edge cases** - What breaks it?
6. **Related files** - Links to related work

**Documentation template:**
```markdown
# [Deliverable Name]

## Purpose
[1-2 sentences about what this is]

## Context
[Why this was created, what problem it solves]

## Usage
[How to use/implement this]

## Examples
[Code, screenshots, or usage examples]

## Edge Cases
[Known limitations, edge cases]

## Related Files
- [Link to related doc 1]
- [Link to related doc 2]
```

---

## Rule 8: Quality Assurance Before Delivery

**Pre-Delivery Checklist (applies to all phases):**

- [ ] Content is in English (unless otherwise specified)
- [ ] Format is .md or appropriate alternative
- [ ] All links are valid
- [ ] Code examples are tested and working
- [ ] Spelling and grammar checked
- [ ] Follows phase-specific guidelines
- [ ] Includes required documentation
- [ ] Has clear structure and organization
- [ ] Addresses the original task completely
- [ ] No sensitive information exposed

**Phase-specific checklists:**
See individual phase AGENT.md files for detailed pre-delivery checklists.

---

## Rule 9: Git Workflow & Commit Messages

**Commit message format (English required):**
```
[Phase] Short description of change

Longer explanation if needed, wrapped at 72 characters.
Include references to related issues or tasks.

Co-Authored-By: Claude [Model] <noreply@anthropic.com>
```

**Examples:**
```
[system_analysis] Add database schema for user authentication

Updated ER diagram and DDL script to support OAuth2 integration.
Includes migration plan and rollback strategy.

[design] Create responsive wireframes for mobile dashboard

Designed 3 breakpoints: mobile (320px), tablet (768px), desktop (1024px).
Added interaction annotations for transitions.

[coding] Fix user session timeout bug

Root cause: Session token expiration not checked on API requests.
Solution: Add middleware to validate token before request processing.
```

---

## Rule 10: Communication Standards

**When communicating with users:**

1. **Be clear about what you're doing**
   - Explicitly state your phase (System Analysis, Design, or Coding)
   - Say what format you're using
   - Explain why you're asking for confirmation

2. **Use structured feedback**
   - Problem statement
   - Impact assessment
   - Proposed solution(s)
   - Recommendation

3. **Provide checkpoints**
   - Check in after major milestones
   - Ask for feedback on direction
   - Confirm before final delivery

4. **Document decisions**
   - Why did you choose this approach?
   - What alternatives were considered?
   - What trade-offs are involved?

**Example communication:**
```
**Phase:** System Analysis
**Format:** Markdown (.md)
**Status:** Draft for review

I've analyzed the requirements and identified 3 architectural options:

**Option A: Monolithic**
- Pros: Simpler deployment
- Cons: Harder to scale individual components
- Time estimate: 2 weeks

**Option B: Microservices**
- Pros: Independent scaling, clear boundaries
- Cons: Complex deployment, network overhead
- Time estimate: 4 weeks

**Option C: Modular Monolith**
- Pros: Balanced approach, moderate complexity
- Cons: Requires careful module management
- Time estimate: 3 weeks

**Recommendation:** Option C provides the best balance for current requirements.

Should I proceed with detailed design for Option C, or would you like to explore others?
```

---

## 🎯 Quick Reference

| Rule | Key Point | When to Use |
|------|-----------|-----------|
| 1 | English is default | All tasks |
| 2 | Markdown format | Documentation, specs |
| 3 | `.agents/` for temp work | During development |
| 4 | Ask before direct edits | Unless task says "edit" |
| 5 | Format by phase | Phase-specific work |
| 6 | Code standards | Coding phase |
| 7 | Full documentation | All deliverables |
| 8 | QA checklist | Before delivery |
| 9 | Git best practices | Commits to repository |
| 10 | Clear communication | All user interactions |

---

## 📞 Questions?

If you're unsure about any rule, check the corresponding phase AGENT.md file or ask for clarification before proceeding.

**Navigate to:**
- [System Analysis AGENT.md](./system_analysis/AGENT.md)
- [Design AGENT.md](./design/AGENT.md)
- [Coding AGENT.md](./coding/AGENT.md)

---

## 📝 Update History

These instructions are living documents. They may be updated as team practices evolve. Always check for the latest version in your repository.

| Date       | Version | Description     | Author | Status           |
| ---------- | ------- | --------------- | ------ | ---------------- |
| 2026-09-20 | 1.0.0   | Initial version | vduczz | Production Ready |

> For the latest updates, check your repository's `.agent-instructions/` directory.
