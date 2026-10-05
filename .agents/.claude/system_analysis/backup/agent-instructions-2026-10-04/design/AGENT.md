# Design Phase - Agent Rules & Procedures

This phase focuses on creating visual designs, user experiences, and interaction models that bridge system analysis and coding.

---

## 🎯 Phase Overview

**Goal:** Create beautiful, intuitive designs that users love and developers can implement.

**When to use this phase:**
- Creating UI mockups and wireframes
- Designing user flows and interactions
- Building design systems and components
- Creating interactive prototypes
- Designing responsive layouts
- Conducting design reviews and handoffs

**Typical workflow:** Understand → Sketch → Design → Prototype → Test → Handoff

**Deliverables:** Wireframes, mockups, prototypes, design systems, component libraries

---

## 4 Mandatory Rules for Design

### Rule 1: User-Centric Design

**The Rule:**
- Every design decision must serve the user
- Understand user goals, not just features
- Test designs with actual users when possible
- Accessibility is not optional, it's mandatory

**How to apply:**
```
For every design, ask:
1. Who is the user?
2. What is their goal?
3. What's the easiest way to achieve it?
4. Can users with disabilities use this?
5. Is this delightful, or just functional?
```

**Example:**
```
❌ Wrong: "Let's put all settings in a dropdown"
✅ Right: "Users need to change 5 settings frequently.
          Let's make those 5 visible, with advanced settings
          in a dropdown. Test with actual users."
```

### Rule 2: Design Consistency

**The Rule:**
- Consistent visual language across the product
- Consistent patterns for common interactions
- Consistent component usage
- Documented design system

**Consistency checklist:**
- [ ] Color palette defined and applied
- [ ] Typography system (font sizes, weights, line heights)
- [ ] Spacing system (margins, padding, gaps)
- [ ] Component library (buttons, inputs, cards, etc.)
- [ ] Interaction patterns (hover, active, disabled states)
- [ ] Icon system (consistent style and sizing)
- [ ] Error/success/warning/info states defined

**Example:**
```
A button should:
- Always look like a button
- React the same way to user interaction
- Use the same spacing and typography
- Work the same across different screens
```

### Rule 3: Accessibility is Mandatory

**The Rule:**
- All designs must be usable by people with disabilities
- Color contrast must meet WCAG AA standards
- Text must be readable (not too small)
- Interactive elements must be keyboard-accessible
- Don't rely on color alone to convey information

**Accessibility checklist:**
- [ ] Color contrast ≥4.5:1 for text
- [ ] Minimum font size 12-14px for body text
- [ ] Focus states visible on interactive elements
- [ ] Icons have text labels or aria-labels
- [ ] Forms have proper labels
- [ ] Modals can be closed with Escape key
- [ ] No content locked behind hover-only
- [ ] Keyboard navigation works

**Example:**
```
❌ Wrong: "Success! (in green text only)"
✅ Right: "✓ Success! (green text + checkmark + clear message)"
```

### Rule 4: Document All Design Decisions

**The Rule:**
- Why did you make this choice?
- What alternatives were considered?
- What constraints influenced this?
- What assumptions are you making?

**Documentation checklist:**
- [ ] Design rationale documented
- [ ] Alternatives considered and compared
- [ ] Constraints acknowledged
- [ ] Assumptions listed
- [ ] Edge cases documented
- [ ] Interactions explained
- [ ] Responsive behavior defined
- [ ] Accessibility approach documented

---

## 7 Task Types with Procedures

### Task Type 1: UI Mockup & Wireframe

**Purpose:** Create visual designs for user interfaces showing layout, components, and interactions.

**Inputs Required:**
- Requirements (what screens are needed)
- User flows (what happens when)
- Design system (if exists)
- Content/copy to display
- Device targets (mobile, tablet, desktop)

**Output Specifications:**
- Wireframes for main flows (low-fidelity)
- Hi-fidelity mockups for key screens
- Responsive variants (mobile, tablet, desktop)
- Component annotations (interaction, states)
- Design specifications (colors, fonts, spacing)

**Procedure:**

1. **Understand Requirements**
   - What screens/pages do we need?
   - What is the user flow?
   - What content needs to be displayed?
   - What constraints exist?

2. **Create Wireframes**
   - Low-fidelity sketches showing layout
   - Focus on structure, not visual design
   - Show information hierarchy
   - Mark interactive elements

3. **Design Mockups**
   - Create high-fidelity mockups from wireframes
   - Apply design system colors, typography, spacing
   - Add visual polish and style
   - Show real content (or realistic placeholders)

4. **Add Annotations**
   - Label interactive elements
   - Document component states (hover, active, disabled)
   - Explain interactions and transitions
   - Note any special behaviors

5. **Create Responsive Variants**
   - Design for multiple breakpoints: mobile (320-480px), tablet (768px), desktop (1024px+)
   - Show how layout adapts
   - Ensure all elements accessible at each breakpoint

6. **Review and Iterate**
   - Share with stakeholders
   - Gather feedback
   - Make revisions
   - Get approval

**Recommended Tools:**
- Figma (recommended)
- Adobe XD
- Sketch
- Penpot (free)

**Pre-Delivery Checklist:**
- [ ] All required screens are wireframed
- [ ] Hi-fidelity mockups created for key flows
- [ ] Responsive variants for 3+ breakpoints
- [ ] Design system components used consistently
- [ ] All interactive elements annotated
- [ ] Color contrast meets WCAG AA
- [ ] Typography is clear and readable
- [ ] Spacing is consistent (using design system)
- [ ] Edge cases handled (empty states, errors, long text)
- [ ] Stakeholder feedback incorporated

**Time estimate:** 3-5 hours per major screen set

---

### Task Type 2: User Flow & Interaction

**Purpose:** Design the complete user journey and interactions for a feature or flow.

**Inputs Required:**
- Feature requirements (what needs to happen)
- User personas (who uses this)
- Happy path (normal workflow)
- Alternative paths (different scenarios)
- Error cases (what can go wrong)

**Output Specifications:**
- User flow diagram (visual)
- Step-by-step interaction guide
- State machine (if applicable)
- Decision trees for complex flows
- Error handling specifications
- Interaction annotations

**Procedure:**

1. **Map the Happy Path**
   - What are the steps to achieve the goal?
   - What information is needed at each step?
   - What decisions must the user make?
   - Create a visual flow showing this path

2. **Identify Alternative Paths**
   - What else could happen?
   - What if the user goes back?
   - What if they skip a step?
   - Add these to the flow diagram

3. **Define Error Cases**
   - What can fail?
   - How should errors be communicated?
   - Can the user recover?
   - Document error handling in flow

4. **Design Transitions**
   - How do we move from step to step?
   - What feedback does the user get?
   - Are there progress indicators?
   - Document transition behavior

5. **Create Interaction Specifications**
   - What happens when user clicks/taps?
   - What form validations are needed?
   - What data is collected?
   - What confirmations are needed?

6. **Review and Test**
   - Walk through flow with team
   - Test with users (if possible)
   - Identify missing pieces
   - Iterate

**Recommended Tools:**
- Mermaid for flow diagrams
- Figma for interactive flows
- FigJam for collaborative design

**Pre-Delivery Checklist:**
- [ ] Happy path clearly documented
- [ ] Alternative paths identified and shown
- [ ] Error handling documented
- [ ] All decision points clear
- [ ] User feedback points defined
- [ ] Form validation rules specified
- [ ] Transitions described
- [ ] Accessibility considerations noted
- [ ] Mobile-specific behaviors documented
- [ ] Team review completed

**Time estimate:** 2-4 hours

---

### Task Type 3: Design System

**Purpose:** Create a comprehensive design system that ensures consistency across the product.

**Inputs Required:**
- Visual brand guidelines
- Product requirements and features
- Existing design (if redesigning)
- Platform targets (web, iOS, Android)

**Output Specifications:**
- Design system documentation
- Component library in Figma
- Color palette (with usage guidelines)
- Typography system
- Spacing/layout grid
- Icon system
- Complete component set with variants

**Procedure:**

1. **Define Design Principles**
   - What values guide our design?
   - What makes our product unique?
   - 3-5 core principles
   - Examples of each principle in action

2. **Create Color Palette**
   - Primary, secondary, accent colors
   - Neutrals (grays for text, backgrounds)
   - Semantic colors (success, error, warning, info)
   - Accessibility: test color contrast

3. **Define Typography System**
   - Font families (1-2 primary)
   - Size scale (8px to 48px)
   - Font weights (300, 400, 600, 700)
   - Line heights (1.2x to 1.8x)
   - Letter spacing adjustments

4. **Create Spacing System**
   - Base unit (8px or 4px)
   - Scale (8, 16, 24, 32, 40, 48, 56, 64px)
   - Application (margins, padding, gaps)
   - Responsive adjustments

5. **Build Component Library**
   - Button (all states and sizes)
   - Input fields (text, select, checkbox, radio)
   - Cards (content containers)
   - Navigation (header, sidebar, breadcrumbs)
   - Modals and overlays
   - Alerts and notifications
   - Forms
   - Tables
   - Pagination
   - Each with: default, hover, active, disabled, error states

6. **Document Everything**
   - Usage guidelines for each component
   - Do's and don'ts
   - Accessibility notes
   - Responsive behavior
   - Code examples (if applicable)

**Recommended Tools:**
- Figma (best for component libraries)
- Storybook (for interactive documentation)
- Zeroheight (design documentation)

**Pre-Delivery Checklist:**
- [ ] Design principles documented and visual examples shown
- [ ] Color palette with all semantic colors
- [ ] Color contrast tested (WCAG AA minimum)
- [ ] Typography system fully defined
- [ ] Spacing system with clear scale
- [ ] All components created with variants
- [ ] Components cover common UI patterns
- [ ] Usage guidelines documented
- [ ] Accessibility guidelines for each component
- [ ] Icon system defined and consistent

**Time estimate:** 8-12 hours

---

### Task Type 4: Prototype & User Testing

**Purpose:** Create interactive prototypes and validate designs with real users.

**Inputs Required:**
- Approved mockups
- User flows to test
- Target users (who will test)
- Key questions to answer

**Output Specifications:**
- Interactive prototype
- User testing plan
- Testing results/findings
- Recommendations based on feedback
- Revised designs

**Procedure:**

1. **Create Prototype**
   - Recreate designs in prototyping tool
   - Add interactions: clicks, transitions, form submissions
   - Include key flows and screens
   - Make it feel realistic

2. **Plan User Testing**
   - Define goals: What do we want to learn?
   - Select users: Who represents our audience?
   - Create scenarios: "Try to [task]"
   - Plan moderation: Questions to ask

3. **Conduct Testing**
   - Recruit 5-8 users (remote or in-person)
   - Guide users through scenarios
   - Observe interactions without bias
   - Ask clarifying questions
   - Record feedback (notes, video if possible)

4. **Analyze Results**
   - What worked well?
   - What confused users?
   - What surprised you?
   - Identify patterns in feedback
   - Quantify if possible (80% found this confusing)

5. **Iterate**
   - Revise designs based on feedback
   - Test critical changes again if major revisions
   - Document what changed and why

**Recommended Tools:**
- Figma (for prototyping)
- UserTesting.com (for recruiting testers)
- Maze (for unmoderated testing)
- Lookback (for recording sessions)

**Pre-Delivery Checklist:**
- [ ] Prototype covers critical paths
- [ ] Prototype is interactive and realistic
- [ ] Testing plan is clear and documented
- [ ] Appropriate number of users tested (5-8 minimum)
- [ ] Testing scenarios align with goals
- [ ] Results documented with evidence
- [ ] Feedback patterns identified
- [ ] Recommendations grounded in user feedback
- [ ] Revisions made based on testing
- [ ] Iterated design tested again (if major changes)

**Time estimate:** 6-8 hours including testing

---

### Task Type 5: Design Tokens & Style Guide

**Purpose:** Extract design decisions into reusable tokens and comprehensive style guide.

**Inputs Required:**
- Approved design system
- Component library
- Design specifications
- Implementation requirements

**Output Specifications:**
- Design tokens file (JSON, YAML, or proprietary format)
- Style guide documentation
- Token naming conventions
- Implementation examples

**Procedure:**

1. **Extract Design Tokens**
   - Colors: Name every color
   - Typography: Define token names for font sizes, weights
   - Spacing: Token names for all spacing values
   - Shadows, borders, radius: Define tokens
   - Create hierarchical naming: category/subcategory/variant

2. **Create Token Structure**
   - Decide on format (JSON, YAML, design tool native)
   - Establish naming conventions
   - Document token categories
   - Example token names:
     ```
     color/primary/base
     color/primary/light
     color/secondary/dark
     typography/body/small
     typography/heading/large
     spacing/8
     spacing/16
     spacing/24
     ```

3. **Document Style Guide**
   - How to use tokens
   - Do's and don'ts
   - Common patterns
   - Examples for each token type
   - Interactive documentation (if possible)

4. **Enable Implementation**
   - Export tokens for development use
   - Create documentation for developers
   - Provide integration guides (CSS, SCSS, JavaScript)

**Recommended Tools:**
- Figma (token management)
- Tokens Studio (for token management)
- Zeroheight (documentation)

**Pre-Delivery Checklist:**
- [ ] All design decisions extracted as tokens
- [ ] Naming conventions consistent and logical
- [ ] Tokens documented with examples
- [ ] Color tokens include contrast information
- [ ] Typography tokens include usage guidelines
- [ ] Spacing tokens cover all common sizes
- [ ] Style guide is comprehensive
- [ ] Developer integration guide provided
- [ ] Token file formats match developer needs
- [ ] Examples showing common patterns

**Time estimate:** 4-6 hours

---

### Task Type 6: Responsive Design

**Purpose:** Adapt designs for different screen sizes ensuring optimal experience across devices.

**Inputs Required:**
- Original design for desktop
- Target breakpoints (mobile, tablet, desktop)
- Content requirements for each size
- Touch interaction requirements (for mobile)

**Output Specifications:**
- Mockups for each breakpoint
- Responsive behavior documented
- Layout shift points documented
- Touch-friendly sizes for mobile
- Viewport guidelines

**Procedure:**

1. **Define Breakpoints**
   - Mobile: 320px, 375px, 480px
   - Tablet: 768px, 1024px
   - Desktop: 1280px+
   - Document which breakpoints matter for your product

2. **Design Mobile Layouts**
   - Start with mobile-first approach
   - Stack content vertically
   - Touch targets: minimum 44x44px
   - Simplify navigation for mobile
   - Consider thumb-friendly areas

3. **Design Tablet Layouts**
   - Adapt to wider screen
   - Multi-column layouts possible
   - Balance between mobile and desktop

4. **Design Desktop Layouts**
   - Full feature set visible
   - Multi-column, wider spacing
   - Complex interactions possible

5. **Specify Transitions**
   - When does layout change?
   - How do elements reflow?
   - Any hidden/shown elements?

6. **Test Responsiveness**
   - View on actual devices if possible
   - Check zoom/scale behavior
   - Test touch interactions
   - Verify text readability at each size

**Recommended Tools:**
- Figma (with responsive components)
- Sketch
- Adobe XD

**Pre-Delivery Checklist:**
- [ ] Designs for 3+ breakpoints provided
- [ ] Breakpoints documented with pixel widths
- [ ] Touch targets ≥44x44px on mobile
- [ ] Text readable without zoom
- [ ] Layout shifts are smooth and logical
- [ ] Navigation adapted for each size
- [ ] Images scale appropriately
- [ ] Whitespace used effectively at each size
- [ ] Tested on actual devices (or browser tools)
- [ ] Responsive behavior documented

**Time estimate:** 3-4 hours

---

### Task Type 7: Design Review & Handoff

**Purpose:** Review final designs, ensure quality, and prepare for developer handoff.

**Inputs Required:**
- Approved final designs
- Design system and tokens
- Component library
- Implementation requirements

**Output Specifications:**
- Design review report
- Developer handoff specification
- Measurement and spacing guide
- Component usage guide
- Asset exports

**Procedure:**

1. **Self-Review**
   - Consistency: Does it follow design system?
   - Completeness: Are all screens designed?
   - Quality: Is it polished?
   - Accessibility: Does it pass WCAG checks?
   - Responsiveness: Does it work at all sizes?
   - Usability: Can users achieve their goals?
   - Identify and fix any issues

2. **Team Review**
   - Present designs to product/engineering team
   - Walk through user flows
   - Clarify design decisions
   - Address questions and concerns
   - Get approval

3. **Create Handoff Spec**
   - Document every screen with annotations
   - Show measurement and spacing
   - Document interactions
   - Explain component usage
   - Specify colors, fonts, sizes
   - Include do's and don'ts

4. **Export Assets**
   - Icons (SVG preferred)
   - Illustrations
   - Images (optimized for web)
   - Component source files
   - Font files if custom fonts

5. **Prepare Documentation**
   - Component usage guide
   - Interaction specifications
   - Accessibility guidelines
   - Animation/transition specifications
   - Error states and edge cases

**Recommended Tools:**
- Figma (for design and handoff)
- Abstract (for version control)
- Zeplin (for design handoff)

**Pre-Delivery Checklist:**
- [ ] All designs reviewed for consistency
- [ ] Design system applied throughout
- [ ] Color contrast verified (WCAG AA)
- [ ] Typography applied consistently
- [ ] Spacing follows grid
- [ ] All interactive elements documented
- [ ] Responsive behavior specified
- [ ] Accessibility requirements documented
- [ ] Interactions and transitions specified
- [ ] Assets exported and organized
- [ ] Developer handoff specification complete
- [ ] Team approval obtained

**Time estimate:** 2-3 hours

---

## Common Mistakes to Avoid

### ❌ Mistake 1: Designing Without Understanding Users

**Problem:** Creating beautiful designs that users don't understand or find hard to use.

**Fix:** Always research users first. Test early and often.

### ❌ Mistake 2: Skipping Accessibility

**Problem:** Designing beautiful interfaces that don't work for people with disabilities.

**Fix:** Accessibility is mandatory. Test with real accessibility tools and users.

### ❌ Mistake 3: Inconsistent Design System Usage

**Problem:** Using different styles, spacings, and components in different parts of the interface.

**Fix:** Build and stick to a design system. Make components reusable.

### ❌ Mistake 4: Poor Responsive Design

**Problem:** Designs that look great on desktop but are unusable on mobile.

**Fix:** Start with mobile, test on actual devices, use proper breakpoints.

### ❌ Mistake 5: Insufficient Documentation

**Problem:** Designs that developers can't implement because they don't understand the intent.

**Fix:** Over-document. Annotate everything. Include reasoning.

---

## Recommended Tools

### Design Tools:
- **Figma** (recommended, collaborative) - Best for teams
- **Adobe XD** - Good Adobe integration
- **Sketch** - Good for macOS users
- **Penpot** (free, open-source) - Great free alternative

### Prototyping:
- **Figma** (built-in)
- **Framer** (interactive)
- **Marvel** (quick prototyping)

### User Testing:
- **UserTesting.com** - Full user research
- **Maze** - Unmoderated testing
- **Lookback** - Video recording

### Accessibility Testing:
- **WAVE** (free) - Color contrast, accessibility checks
- **Axe DevTools** (free) - Accessibility audit
- **Contrast Checker** (free) - Color contrast

### Collaboration:
- **Figma** - Built-in commenting
- **FigJam** - Collaborative whiteboarding
- **Slack** - Team communication

---

## Phase Navigation

**Before you start:** Read [COMMON-RULES.md](../COMMON-RULES.md)

**After design is approved:** Move to [Coding Phase](../coding/AGENT.md)

**If you need analysis:** Reference [System Analysis Phase](../system_analysis/AGENT.md)

**Questions?** Check [INDEX.md](../INDEX.md) or ask your team lead
