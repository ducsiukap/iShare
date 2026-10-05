# Coding Phase - Agent Rules & Procedures

This phase focuses on implementing features, fixing bugs, testing, and deploying code that meets quality standards.

---

## 🎯 Phase Overview

**Goal:** Write high-quality, well-tested, maintainable code that follows specifications and best practices.

**When to use this phase:**
- Implementing new features
- Fixing bugs
- Writing and running tests
- Refactoring code
- Optimizing performance
- Creating database migrations
- Deploying to production

**Typical workflow:** Spec → Plan → Tests → Code → Review → Deploy

**Deliverables:** Source code, tests, documentation, git commits, pull requests

---

## 5 Mandatory Rules for Coding

### Rule 1: Code Quality First

**The Rule:**
- Quality matters more than speed
- Follow the project's coding standards
- Write clean, readable, maintainable code
- Use consistent naming and structure
- Refactor as you go (don't leave technical debt)

**Code quality checklist:**
- [ ] Code is readable (clear variable names, short functions)
- [ ] Cyclomatic complexity < 10 per function
- [ ] No code duplication (< 3% duplication)
- [ ] Functions are focused (do one thing well)
- [ ] Error handling is explicit
- [ ] Follows project style guide
- [ ] Uses consistent patterns
- [ ] Comments explain "why", not "what"

**Example:**
```javascript
// ❌ Bad: Complex, unclear intent
function process(a, b, c) {
  let x = a.map(v => v * 2).filter(v => v > c);
  return x.length > b ? x.slice(0, b) : x;
}

// ✅ Good: Clear intent, focused, well-named
function getTopPrioritiesUnderThreshold(items, maxCount, threshold) {
  const priorityItems = items
    .filter(item => item.priority <= threshold)
    .map(item => ({...item, priorityScore: item.priority * 2}))
    .sort((a, b) => b.priorityScore - a.priorityScore);
  
  return priorityItems.slice(0, maxCount);
}
```

### Rule 2: Test Coverage > 80%

**The Rule:**
- Write tests BEFORE or ALONGSIDE code (TDD)
- Aim for >80% code coverage
- Test happy path, edge cases, and errors
- Tests must pass before code is merged
- Keep tests fast and reliable

**Testing checklist:**
- [ ] Unit tests for all functions
- [ ] Integration tests for major flows
- [ ] Edge cases tested
- [ ] Error cases tested
- [ ] Coverage > 80%
- [ ] Tests run in < 30 seconds
- [ ] All tests pass
- [ ] No flaky tests (tests that sometimes fail)

**Example test structure:**
```javascript
describe('UserService', () => {
  describe('createUser', () => {
    it('should create user with valid email', () => {
      const result = createUser('test@example.com', 'password123');
      expect(result.id).toBeDefined();
      expect(result.email).toBe('test@example.com');
    });
    
    it('should reject user with invalid email', () => {
      expect(() => createUser('invalid', 'password'))
        .toThrow('Invalid email format');
    });
    
    it('should hash password', () => {
      const result = createUser('test@example.com', 'password');
      expect(result.password).not.toBe('password');
    });
  });
});
```

### Rule 3: Follow the Specification

**The Rule:**
- Understand requirements before coding
- Implement exactly what was specified
- No scope creep (additional features not in spec)
- Clarify ambiguities before coding
- Test against acceptance criteria

**Specification adherence checklist:**
- [ ] Understood all requirements before starting
- [ ] Clarified ambiguous requirements
- [ ] Implementation matches specification
- [ ] All acceptance criteria met
- [ ] No additional features added (scope creep)
- [ ] Constraints (performance, security) met
- [ ] Edge cases from spec handled

**Example:**
```
Spec: "Users can search for posts by title"

✅ Implementation should:
- Accept search query (text)
- Return matching posts
- Case-insensitive matching
- Return empty array if no matches
- Support special characters in titles

❌ Don't implement:
- Filter by author (not in spec)
- Full-text search (not in spec)
- Save search history (not in spec)
```

### Rule 4: Performance & Security Matter

**The Rule:**
- Performance targets must be met
- Security vulnerabilities must be fixed
- Code must handle errors gracefully
- Sensitive data must be protected
- Assume malicious input

**Performance & security checklist:**
- [ ] API responses < 200ms (target)
- [ ] Page load time < 3s (target)
- [ ] Database queries < 100ms (target)
- [ ] No SQL injection vulnerabilities
- [ ] No XSS vulnerabilities
- [ ] Passwords hashed (bcrypt, scrypt)
- [ ] Sensitive data encrypted
- [ ] Input validation on all endpoints
- [ ] Rate limiting implemented
- [ ] Logging for audit trails

**Security example:**
```javascript
// ❌ Bad: SQL injection, no password hashing
function loginUser(email, password) {
  const query = `SELECT * FROM users WHERE email='${email}' AND password='${password}'`;
  return db.query(query);
}

// ✅ Good: Parameterized query, hashed password, error handling
async function loginUser(email, password) {
  const user = await db.query(
    'SELECT * FROM users WHERE email = $1',
    [email]
  );
  
  if (!user) throw new Error('User not found');
  
  const isValid = await bcrypt.compare(password, user.passwordHash);
  if (!isValid) throw new Error('Invalid password');
  
  return user;
}
```

### Rule 5: Document & Communicate

**The Rule:**
- Code must be self-documenting (clear names, structure)
- Complex logic must have comments explaining "why"
- Functions/classes must have documentation
- Git commits must explain changes
- Pull requests must be clear and reviewable

**Documentation checklist:**
- [ ] README updated (if applicable)
- [ ] API endpoints documented
- [ ] Complex algorithms explained in comments
- [ ] Function/method documentation included
- [ ] Edge cases documented
- [ ] Dependencies listed
- [ ] Setup instructions clear
- [ ] Git commit messages are descriptive
- [ ] PR description explains "why" and "what"

---

## 8 Task Types with Procedures

### Task Type 1: Feature Implementation

**Purpose:** Implement a complete feature from specification to production.

**Inputs Required:**
- Feature specification
- Acceptance criteria
- Design specifications (if applicable)
- Performance and security requirements
- Deployment plan

**Output Specifications:**
- Source code (meeting quality standards)
- Unit tests (>80% coverage)
- Integration tests
- Documentation updates
- Git commits
- Pull request with clear description

**Procedure:**

1. **Understand the Feature**
   - Read specification completely
   - Ask clarifying questions
   - Identify edge cases
   - Break into smaller tasks
   - Plan implementation order

2. **Plan the Implementation**
   - Create task list
   - Estimate time per task
   - Identify dependencies
   - Plan testing strategy
   - Identify risks

3. **Write Tests First**
   - Write unit tests for functions
   - Write integration tests for flows
   - Test edge cases and errors
   - Tests should fail initially (TDD)

4. **Implement Feature**
   - Make tests pass one by one
   - Keep tests green throughout
   - Follow code quality standards
   - Add documentation as you go
   - Commit frequently

5. **Code Review**
   - Self-review for quality
   - Check test coverage
   - Verify against specification
   - Get peer review
   - Address feedback

6. **Deploy**
   - Merge to main branch
   - Run full test suite
   - Deploy to staging
   - Test in staging
   - Deploy to production
   - Monitor for errors

**Recommended Tools:**
- Git (version control)
- Jest, Mocha (testing)
- ESLint (code quality)
- GitHub/GitLab (PR management)

**Pre-Delivery Checklist:**
- [ ] Feature fully implemented per specification
- [ ] All acceptance criteria met
- [ ] Tests written (>80% coverage)
- [ ] All tests passing
- [ ] Code reviewed by peer
- [ ] Code quality standards met
- [ ] No security vulnerabilities
- [ ] Performance targets met
- [ ] Documentation updated
- [ ] Ready for production deployment

**Time estimate:** 4-8 hours

---

### Task Type 2: Bug Fix

**Purpose:** Identify and fix a bug in production or staging code.

**Inputs Required:**
- Bug description / reproduction steps
- Expected behavior
- Current behavior
- Affected users / impact
- Production or staging environment

**Output Specifications:**
- Root cause analysis
- Fixed code
- Regression tests
- Git commit explaining fix
- Verification that bug is resolved

**Procedure:**

1. **Understand the Bug**
   - Reproduce the bug (follow exact steps)
   - Verify it's actually a bug (not user error)
   - Determine severity
   - Identify affected systems

2. **Analyze Root Cause**
   - Where in the code does this happen?
   - Why does it happen?
   - Is this a logic error, race condition, edge case?
   - Could this affect other features?

3. **Create Fix**
   - Write test that reproduces bug (should fail)
   - Fix the code (make test pass)
   - Verify fix doesn't break other tests
   - Check for similar issues elsewhere

4. **Regression Testing**
   - Add test to prevent regression
   - Test related features
   - Test on affected browsers/devices (if applicable)
   - Verify fix in staging

5. **Document**
   - Write clear commit message
   - Explain root cause in commit/PR
   - Link to bug report
   - Document if this affects other systems

6. **Deploy**
   - Code review
   - Merge to main
   - Deploy to production
   - Monitor for issues

**Recommended Tools:**
- Git (version control)
- Testing tools (Jest, Mocha)
- Logging/monitoring tools
- Browser DevTools (for client-side bugs)

**Pre-Delivery Checklist:**
- [ ] Bug is reproduced consistently
- [ ] Root cause identified and documented
- [ ] Fix implemented and tested
- [ ] Regression test added
- [ ] No new issues introduced
- [ ] Related features tested
- [ ] Clear commit message
- [ ] Staging verified
- [ ] Ready for production
- [ ] Monitoring plan for production

**Time estimate:** 1-3 hours

---

### Task Type 3: Code Review

**Purpose:** Review pull request for quality, correctness, performance, and security.

**Inputs Required:**
- Pull request with code changes
- Description of changes
- Related specification
- Tests included in PR

**Output Specifications:**
- Detailed code review comments
- Approval or requests for changes
- Suggestions for improvement
- Security/performance concerns flagged

**Procedure:**

1. **Understand the Change**
   - Read PR description
   - Understand the feature/fix
   - Check against specification
   - Review related code

2. **Check Code Quality**
   - Readability: Can you understand it?
   - Naming: Are variables/functions well-named?
   - Structure: Is it well-organized?
   - Duplication: Is there code duplication?
   - Complexity: Any overly complex functions?

3. **Verify Tests**
   - Are tests comprehensive?
   - Coverage > 80%?
   - Edge cases tested?
   - Do tests make sense?

4. **Check for Security Issues**
   - SQL injection vulnerabilities?
   - XSS vulnerabilities?
   - Sensitive data exposed?
   - Authentication/authorization correct?
   - Input validation present?

5. **Check Performance**
   - No N+1 queries?
   - No unnecessary loops?
   - Efficient algorithms?
   - Large data sets handled efficiently?

6. **Provide Feedback**
   - Positive feedback on good work
   - Specific, constructive criticism
   - Suggestions for improvement
   - Questions about unclear code
   - Approval or requests for changes

**Recommended Tools:**
- GitHub/GitLab (PR review)
- SonarQube (code quality analysis)
- OWASP tools (security scanning)

**Pre-Delivery Checklist:**
- [ ] Understood the change and requirements
- [ ] Code quality standards met
- [ ] Test coverage >80%
- [ ] No security vulnerabilities
- [ ] Performance is acceptable
- [ ] Clear, constructive feedback provided
- [ ] All concerns documented
- [ ] Approval given or changes requested

**Time estimate:** 1-2 hours

---

### Task Type 4: Performance Optimization

**Purpose:** Identify bottlenecks and optimize code/systems for better performance.

**Inputs Required:**
- Performance requirements (target response time, throughput)
- Current performance metrics
- Identified bottleneck (if known)
- Load profile (expected usage)

**Output Specifications:**
- Root cause analysis
- Optimization implemented
- Measurable performance improvement
- Before/after metrics
- Tests to prevent regression

**Procedure:**

1. **Measure Current Performance**
   - Baseline metrics (response time, throughput, resource usage)
   - Identify worst performing queries/functions
   - Use profiler to find bottlenecks
   - Document current performance

2. **Identify Root Cause**
   - Is it database queries?
   - Algorithm complexity?
   - Memory usage?
   - I/O operations?
   - Third-party API calls?

3. **Plan Optimization**
   - List possible optimizations
   - Estimate improvement for each
   - Choose high-impact optimizations
   - Consider trade-offs

4. **Implement**
   - Make one optimization at a time
   - Measure impact
   - Keep tests passing
   - Document changes

5. **Verify**
   - Run performance tests
   - Compare before/after
   - Ensure tests still pass
   - No regressions in other areas

6. **Deploy and Monitor**
   - Deploy to staging first
   - Verify performance improvement
   - Deploy to production
   - Monitor real-world performance

**Optimization strategies:**
- Database: Add indexes, denormalize, query optimization
- Code: Caching, lazy loading, algorithm improvements
- Infrastructure: Load balancing, CDN, database replicas
- Frontend: Image optimization, lazy loading, code splitting

**Pre-Delivery Checklist:**
- [ ] Current performance measured
- [ ] Bottleneck identified
- [ ] Optimization strategy defined
- [ ] Implementation complete
- [ ] Measurable improvement achieved
- [ ] Tests still passing
- [ ] No regressions
- [ ] Monitoring plan
- [ ] Documentation updated

**Time estimate:** 3-6 hours

---

### Task Type 5: Refactoring

**Purpose:** Improve code quality, maintainability, and structure without changing functionality.

**Inputs Required:**
- Code to refactor
- Reason for refactoring (why this matters)
- Areas of focus (e.g., reduce duplication, improve naming)

**Output Specifications:**
- Refactored code
- Improved structure/clarity
- All tests still passing
- No functional changes
- Commit explaining refactoring

**Procedure:**

1. **Understand Current Code**
   - Read code completely
   - Understand what it does
   - Identify pain points
   - Note areas for improvement

2. **Establish Test Coverage**
   - Write tests for current behavior
   - Tests must pass before refactoring
   - >80% coverage on code being refactored
   - Tests are your safety net

3. **Refactor Incrementally**
   - Make one small change at a time
   - Run tests after each change
   - Commit after each logical step
   - Keep tests green always

4. **Refactoring Strategies**
   - Extract functions (reduce duplication)
   - Rename for clarity
   - Reduce complexity
   - Improve structure
   - Simplify conditional logic

5. **Verify**
   - All original tests pass
   - Functionality unchanged
   - Code is cleaner and clearer
   - Performance unchanged

6. **Document**
   - Commit messages explain what changed
   - Note why refactoring was needed

**Example refactoring:**
```javascript
// Before: Duplicated logic
function getUserInfo(userId) {
  const user = db.query(`SELECT * FROM users WHERE id = ${userId}`);
  return {
    name: user.name,
    email: user.email,
    verified: user.verified
  };
}

function getAdminInfo(userId) {
  const user = db.query(`SELECT * FROM users WHERE id = ${userId}`);
  return {
    name: user.name,
    email: user.email,
    verified: user.verified,
    role: user.role
  };
}

// After: Extracted common logic
function getUserById(userId) {
  return db.query('SELECT * FROM users WHERE id = $1', [userId]);
}

function getUserInfo(userId) {
  const user = getUserById(userId);
  return pick(user, ['name', 'email', 'verified']);
}

function getAdminInfo(userId) {
  const user = getUserById(userId);
  return pick(user, ['name', 'email', 'verified', 'role']);
}
```

**Pre-Delivery Checklist:**
- [ ] Current tests passing (before refactoring)
- [ ] Tests still passing (after refactoring)
- [ ] Code is cleaner/clearer
- [ ] Functionality completely unchanged
- [ ] No performance impact
- [ ] Commit messages explain refactoring
- [ ] Complexity reduced
- [ ] Duplication eliminated

**Time estimate:** 3-5 hours

---

### Task Type 6: Testing

**Purpose:** Write comprehensive tests covering functionality, edge cases, and error scenarios.

**Inputs Required:**
- Code to test
- Requirements/spec
- Edge cases to consider
- Error scenarios to test

**Output Specifications:**
- Unit tests for functions
- Integration tests for flows
- Test coverage >80%
- All tests passing
- Edge cases documented

**Procedure:**

1. **Plan Test Strategy**
   - What needs to be tested?
   - What are edge cases?
   - What error scenarios?
   - How will you test each?

2. **Write Unit Tests**
   - Test each function independently
   - Test happy path
   - Test edge cases
   - Test error cases
   - Aim for >80% coverage

3. **Write Integration Tests**
   - Test major workflows
   - Test system interactions
   - Test data flows
   - Test error recovery

4. **Write E2E Tests** (if applicable)
   - Test complete user journeys
   - Test across different browsers (if web)
   - Test on different devices (if mobile)

5. **Test Edge Cases**
   - Empty inputs
   - Very large inputs
   - Special characters
   - Null/undefined values
   - Race conditions
   - Concurrent access

6. **Verify Test Quality**
   - Tests are independent
   - Tests are repeatable
   - Tests are fast
   - Tests are clear
   - Tests fail when code is broken

**Testing tools:**
- Unit: Jest, Mocha, RSpec
- Integration: Integration test framework
- E2E: Cypress, Playwright, Selenium
- Coverage: Jest, Istanbul

**Pre-Delivery Checklist:**
- [ ] Unit tests for all functions
- [ ] Integration tests for major flows
- [ ] Edge cases tested
- [ ] Error scenarios tested
- [ ] Coverage >80%
- [ ] All tests passing
- [ ] Tests are fast (<30s for full suite)
- [ ] No flaky tests
- [ ] Tests are well-organized
- [ ] Comments explain complex tests

**Time estimate:** 3-6 hours

---

### Task Type 7: Database Migration

**Purpose:** Safely modify database schema with zero data loss.

**Inputs Required:**
- Current schema
- Desired schema
- Data migration requirements
- Rollback plan

**Output Specifications:**
- Up migration script
- Down migration script
- Data migration plan
- Rollback procedures
- Testing results

**Procedure:**

1. **Plan Migration**
   - What schema changes are needed?
   - How will existing data be migrated?
   - What's the rollback plan?
   - Is downtime required?

2. **Write Up Migration**
   - Add new tables/columns
   - Add indexes
   - Add constraints
   - Migrate existing data (if needed)
   - Keep this atomic when possible

3. **Write Down Migration**
   - Reverse all changes
   - Drop new columns/tables
   - Restore old constraints
   - Reverse data changes

4. **Handle Data Migration**
   - Backup data before migration
   - Migrate existing data safely
   - Verify data integrity
   - Check constraints

5. **Test Migration**
   - Test on copy of production data
   - Verify data integrity
   - Test rollback
   - Verify rollback works
   - Check performance impact

6. **Deploy**
   - Backup production database
   - Run migration on staging
   - Verify on staging
   - Schedule production migration
   - Run migration
   - Verify success
   - Monitor for issues

**Example migration:**
```sql
-- Up migration: Add new user status column
BEGIN;

ALTER TABLE users ADD COLUMN status VARCHAR(20) DEFAULT 'active';
UPDATE users SET status = 'active' WHERE verified = true;
UPDATE users SET status = 'pending' WHERE verified = false;
ALTER TABLE users DROP COLUMN verified;
CREATE INDEX idx_users_status ON users(status);

COMMIT;

-- Down migration: Revert to verified column
BEGIN;

ALTER TABLE users ADD COLUMN verified BOOLEAN DEFAULT FALSE;
UPDATE users SET verified = true WHERE status = 'active';
UPDATE users SET verified = false WHERE status = 'pending';
DROP INDEX idx_users_status;
ALTER TABLE users DROP COLUMN status;

COMMIT;
```

**Pre-Delivery Checklist:**
- [ ] Schema changes clearly documented
- [ ] Data migration plan detailed
- [ ] Rollback plan tested
- [ ] Up migration script working
- [ ] Down migration script working
- [ ] Data integrity verified
- [ ] Performance impact acceptable
- [ ] Tested on production data copy
- [ ] Backup procedure documented
- [ ] Monitoring plan for production

**Time estimate:** 4-8 hours

---

### Task Type 8: API Implementation

**Purpose:** Implement a complete REST API endpoint with validation, error handling, and documentation.

**Inputs Required:**
- API specification (OpenAPI/Swagger)
- Request/response examples
- Authentication requirements
- Performance targets

**Output Specifications:**
- Working API endpoint
- Input validation
- Error handling
- Complete tests
- API documentation
- Git commits

**Procedure:**

1. **Understand Specification**
   - Read API spec
   - Understand request format
   - Understand response format
   - Understand error cases

2. **Design the Implementation**
   - Identify data sources
   - Plan validation
   - Plan error handling
   - Identify dependencies

3. **Implement Endpoint**
   - Create route handler
   - Implement request parsing
   - Implement business logic
   - Implement response formatting

4. **Add Validation**
   - Validate request parameters
   - Validate data types
   - Validate required fields
   - Return clear error messages

5. **Add Error Handling**
   - Handle missing resources (404)
   - Handle invalid input (400)
   - Handle authentication errors (401)
   - Handle authorization errors (403)
   - Handle server errors (500)
   - Return consistent error format

6. **Write Tests**
   - Happy path test
   - Invalid input tests
   - Missing field tests
   - Not found tests
   - Authentication tests
   - >80% coverage

7. **Document**
   - Update API documentation
   - Document error codes
   - Provide example requests/responses
   - Document rate limiting

**Example API endpoint:**
```javascript
/**
 * GET /api/users/:id
 * 
 * Get a user by ID
 * 
 * @param {number} id - User ID (required)
 * @returns {User} User object
 * @throws {404} User not found
 * @throws {401} Unauthorized
 */
router.get('/users/:id', authenticate, async (req, res) => {
  try {
    const userId = parseInt(req.params.id);
    
    // Validate input
    if (!Number.isInteger(userId) || userId <= 0) {
      return res.status(400).json({
        error: 'INVALID_USER_ID',
        message: 'User ID must be a positive integer'
      });
    }
    
    // Get user
    const user = await User.findById(userId);
    if (!user) {
      return res.status(404).json({
        error: 'USER_NOT_FOUND',
        message: `User with ID ${userId} not found`
      });
    }
    
    // Check authorization
    if (req.user.id !== userId && !req.user.isAdmin) {
      return res.status(403).json({
        error: 'FORBIDDEN',
        message: 'You do not have permission to view this user'
      });
    }
    
    res.json(user);
  } catch (error) {
    console.error('Error fetching user:', error);
    res.status(500).json({
      error: 'INTERNAL_SERVER_ERROR',
      message: 'An error occurred while fetching the user'
    });
  }
});
```

**Pre-Delivery Checklist:**
- [ ] Endpoint fully implemented per spec
- [ ] Input validation on all fields
- [ ] Error handling for all scenarios
- [ ] Error messages are clear
- [ ] Authentication check (if required)
- [ ] Authorization check (if required)
- [ ] Response format matches spec
- [ ] Tests >80% coverage
- [ ] All tests passing
- [ ] Performance within target
- [ ] Documentation complete

**Time estimate:** 3-5 hours

---

## Quality Standards & Metrics

### Code Quality Targets
- **Test Coverage:** >80%
- **Cyclomatic Complexity:** <10 per function
- **Code Duplication:** <3%
- **Security Grade:** A (no vulnerabilities)
- **Linter Issues:** 0 critical, <5 warnings

### Performance Targets
- **API Response Time:** <200ms (target)
- **Page Load Time:** <3s (target)
- **Database Query:** <100ms (target)
- **Error Rate:** <0.1% (target)

### Testing Standards
- Minimum 80% coverage
- Unit tests for all functions
- Integration tests for major flows
- No flaky tests
- Tests run in <30 seconds

---

## Common Mistakes to Avoid

### ❌ Mistake 1: No Tests (or Insufficient Tests)

**Problem:** Code without tests is broken code waiting to happen.

**Fix:** Write tests FIRST. Aim for >80% coverage. Test edge cases.

### ❌ Mistake 2: Ignoring Error Handling

**Problem:** Code that only handles the happy path fails in production.

**Fix:** Handle all error cases. Provide clear error messages. Log errors.

### ❌ Mistake 3: Skipping Security Review

**Problem:** Security vulnerabilities end up in production.

**Fix:** Always think security. Validate inputs. Use parameterized queries. Check OWASP top 10.

### ❌ Mistake 4: Unclear Commits and PRs

**Problem:** Team members don't understand what changed or why.

**Fix:** Write clear commit messages. Explain "why" in PRs. Reference requirements.

### ❌ Mistake 5: Not Following Specification

**Problem:** Implementing features that weren't requested or missing required features.

**Fix:** Clarify requirements. Stick to specification. Ask questions before coding.

---

## Recommended Tools

### Version Control:
- Git
- GitHub/GitLab (PR management)
- Conventional Commits (commit format)

### Testing:
- Jest (JavaScript)
- Mocha (JavaScript)
- RSpec (Ruby)
- pytest (Python)
- Mockito (Java)

### Code Quality:
- ESLint (JavaScript linting)
- SonarQube (comprehensive analysis)
- Prettier (code formatting)
- Istanbul (coverage reporting)

### Security:
- OWASP ZAP (security scanning)
- Dependabot (dependency vulnerabilities)
- SonarQube (security issues)

### Performance:
- Chrome DevTools (profiling)
- New Relic (monitoring)
- DataDog (APM)
- Artillery (load testing)

### Documentation:
- Swagger/OpenAPI (API docs)
- JSDoc (code documentation)
- Markdown (guides and READMEs)

---

## Phase Navigation

**Before you start:** Read [COMMON-RULES.md](../COMMON-RULES.md)

**After coding is complete:** Get code review and prepare for deployment

**If you need design:** Reference [Design Phase](../design/AGENT.md)

**If you need analysis:** Reference [System Analysis Phase](../system_analysis/AGENT.md)

**Questions?** Check [README.md](../README.md) or ask your team lead
